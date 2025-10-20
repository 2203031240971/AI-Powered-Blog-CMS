from django.db import models
from django.utils.text import slugify
from apps.users.models import User

class Category(models.Model):
    """Blog categories."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Blog(models.Model):
    """Blog post model."""
    
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=300, blank=True)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='blogs')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    views_count = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['status', '-published_at']),
            models.Index(fields=['author', 'status']),
        ]
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    @property
    def ai_summary(self):
        """Get AI-generated summary if available."""
        try:
            return self.ai_summary_record.summary
        except:
            return None


class BlogSummary(models.Model):
    """AI-generated blog summary."""
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, related_name='ai_summary_record')
    summary = models.TextField()
    key_points = models.JSONField(default=list)
    sentiment = models.CharField(max_length=20, blank=True)  # positive, negative, neutral
    generated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Blog Summary'
        verbose_name_plural = 'Blog Summaries'
    
    def __str__(self):
        return f"Summary for {self.blog.title}"


class Comment(models.Model):
    """Blog comments."""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['blog', 'is_approved']),
        ]
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.blog.title}"


class Tag(models.Model):
    """Blog tags for categorization."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    blogs = models.ManyToManyField(Blog, related_name='tags')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
