from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Custom user model with role-based access control."""
    
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Administrator'
        EDITOR = 'editor', 'Editor'
        AUTHOR = 'author', 'Author'
        VIEWER = 'viewer', 'Viewer'
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )
    
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.VIEWER
    )
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    is_active_user = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    def has_permission(self, permission):
        """Check if user has specific permission based on role."""
        permissions = {
            'admin': ['create', 'read', 'update', 'delete', 'manage_users'],
            'editor': ['create', 'read', 'update', 'delete'],
            'author': ['create', 'read', 'update'],
            'viewer': ['read'],
        }
        return permission in permissions.get(self.role, [])
