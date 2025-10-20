from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """Serializer for user model."""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 
                  'bio', 'profile_image', 'is_active_user', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class UserCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating new users with password validation."""
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name', 'role']
    
    def validate(self, data):
        if data['password'] != data.pop('password2'):
            raise serializers.ValidationError({'password': "Passwords don't match."})
        return data
    
    def create(self, validated_data):
        # Remove password from validated_data
        password = validated_data.pop('password')
        
        # Create user without password first
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role=validated_data.get('role', 'viewer'),
            is_active=True
        )
        
        # Set password properly (this hashes it)
        user.set_password(password)
        user.save()
        
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    """Serializer for user detail with all fields."""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 
                  'bio', 'profile_image', 'is_active_user', 'is_staff', 'is_superuser',
                  'created_at', 'updated_at']
