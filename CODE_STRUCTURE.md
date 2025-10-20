# 📁 Code Structure & Organization

## 🏗️ **Complete Project Structure**

This document explains the architecture and organization of both the Django backend and React frontend codebases.

---

## 📂 **Project Root Structure**

```
AI-powered Blog CMS/
│
├── backend/                    # Django REST Framework Backend
│   ├── apps/                   # Django applications
│   ├── config/                 # Project configuration
│   ├── logs/                   # Application logs
│   ├── media/                  # User-uploaded files
│   ├── static/                 # Static files (CSS, JS, images)
│   ├── db.sqlite3             # SQLite database (development)
│   ├── manage.py              # Django management script
│   └── requirements.txt       # Python dependencies
│
├── frontend/                   # React Frontend Application
│   ├── public/                 # Public assets
│   ├── src/                    # Source code
│   ├── package.json           # npm dependencies
│   ├── tailwind.config.js     # Tailwind CSS configuration
│   └── postcss.config.js      # PostCSS configuration
│
├── docker/                     # Docker configuration files
│   ├── Dockerfile.backend     # Backend container
│   └── Dockerfile.frontend    # Frontend container
│
├── ci-cd/                      # CI/CD pipeline configurations
│   └── github-actions/        # GitHub Actions workflows
│
├── docker-compose.yml         # Multi-container orchestration
├── .gitignore                 # Git ignore rules
└── README.md                  # Project documentation
```

---

## 🐍 **Django Backend Structure**

### **Directory Overview**

```
backend/
│
├── apps/                       # Modular Django applications
│   ├── __init__.py
│   │
│   ├── users/                  # User management & authentication
│   │   ├── __init__.py
│   │   ├── admin.py           # Admin panel configuration
│   │   ├── apps.py            # App configuration
│   │   ├── models.py          # User model
│   │   ├── serializers.py     # DRF serializers
│   │   ├── urls.py            # URL routing
│   │   ├── views.py           # API views
│   │   ├── permissions.py     # Custom permissions
│   │   └── migrations/        # Database migrations
│   │
│   ├── blogs/                  # Blog content management
│   │   ├── __init__.py
│   │   ├── admin.py           # Blog admin interface
│   │   ├── apps.py
│   │   ├── models.py          # Blog, Category, Tag, Comment models
│   │   ├── serializers.py     # Blog serializers
│   │   ├── urls.py
│   │   ├── views.py           # Blog CRUD operations
│   │   ├── filters.py         # Query filtering
│   │   ├── pagination.py      # Custom pagination
│   │   └── migrations/
│   │
│   └── ai_service/             # AI integration & processing
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py          # AITask, BlogSummary models
│       ├── serializers.py
│       ├── service.py         # OpenAI API integration
│       ├── tasks.py           # Celery async tasks
│       ├── urls.py
│       ├── views.py
│       └── migrations/
│
├── config/                     # Project configuration
│   ├── __init__.py
│   ├── settings.py            # Django settings
│   ├── urls.py                # Root URL configuration
│   ├── wsgi.py                # WSGI application
│   ├── asgi.py                # ASGI application
│   └── celery.py              # Celery configuration
│
├── logs/                       # Application logs
│   ├── django.log
│   ├── error.log
│   └── api.log
│
├── media/                      # User uploads
│   ├── blog_images/
│   ├── user_avatars/
│   └── documents/
│
├── static/                     # Static files
│   ├── css/
│   ├── js/
│   └── images/
│
├── manage.py                   # Django CLI
├── requirements.txt            # Dependencies
├── .env                        # Environment variables
└── pytest.ini                 # Test configuration
```

---

## 📄 **Backend File Explanations**

### **1. config/settings.py**

**Purpose:** Central configuration for the entire Django project.

**Key Sections:**

```python
# Security
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')

# Custom User Model
AUTH_USER_MODEL = 'users.User'

# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'apps.users',
    'apps.blogs',
    'apps.ai_service',
]

# REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# JWT Settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'ALGORITHM': 'HS256',
}

# CORS Configuration
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# OpenAI Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
```

**Why It Matters:**
- Controls all project behavior
- Security settings
- Database configuration
- API authentication
- Third-party integrations

---

### **2. apps/users/models.py**

**Purpose:** Defines the User model with custom fields and role-based access.

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    Adds role-based access control and additional profile fields.
    """
    
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('author', 'Author'),
        ('reader', 'Reader'),
    )
    
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='reader',
        help_text="User role for permission management"
    )
    
    bio = models.TextField(
        blank=True,
        null=True,
        help_text="User biography"
    )
    
    profile_picture = models.ImageField(
        upload_to='user_avatars/',
        blank=True,
        null=True
    )
    
    # Fix ManyToMany field clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.username
    
    @property
    def is_author(self):
        return self.role in ['author', 'admin']
    
    @property
    def is_admin_user(self):
        return self.role == 'admin'
```

**Key Features:**
- Extends Django's AbstractUser
- Role-based permissions (admin, author, reader)
- Custom profile fields (bio, profile picture)
- Helper properties for permission checks

---

### **3. apps/users/serializers.py**

**Purpose:** Convert User model instances to/from JSON for API responses.

```python
from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Handles password hashing and validation.
    """
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password2', 
                  'first_name', 'last_name', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    def validate(self, attrs):
        """Ensure passwords match"""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Passwords don't match."}
            )
        return attrs
    
    def create(self, validated_data):
        """
        Create user with hashed password.
        CRITICAL: Use create_user() not create() to hash password.
        """
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        user.is_active = True  # Activate user immediately
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile display"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 
                  'role', 'bio', 'profile_picture', 'created_at']
        read_only_fields = ['id', 'created_at']
```

**Why It's Important:**
- Handles password hashing (security!)
- Validates input data
- Converts models to JSON
- Controls what fields are exposed in API

---

### **4. apps/blogs/models.py**

**Purpose:** Define blog content models and relationships.

```python
from django.db import models
from django.utils.text import slugify
from apps.users.models import User

class Category(models.Model):
    """Blog categories for organization"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    """Tags for blog posts"""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Blog(models.Model):
    """Main blog post model"""
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    excerpt = models.CharField(max_length=300, blank=True)
    
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blogs'
    )
    
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='blogs'
    )
    
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='blogs'
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )
    
    featured_image = models.ImageField(
        upload_to='blog_images/',
        blank=True,
        null=True
    )
    
    views_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['status']),
            models.Index(fields=['-created_at']),
        ]
    
    def save(self, *args, **kwargs):
        # Auto-generate slug from title
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def increment_views(self):
        """Increment view count"""
        self.views_count += 1
        self.save(update_fields=['views_count'])


class Comment(models.Model):
    """Comments on blog posts"""
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    
    content = models.TextField(max_length=1000)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )
    
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.blog.title}"
```

**Database Relationships:**
- `Blog` → `User` (Many-to-One): Each blog has one author
- `Blog` → `Category` (Many-to-One): Each blog has one category
- `Blog` ↔ `Tag` (Many-to-Many): Blogs can have multiple tags
- `Blog` → `Comment` (One-to-Many): Blogs can have many comments
- `Comment` → `Comment` (Self-referential): Comments can have replies

---

### **5. apps/ai_service/models.py**

**Purpose:** AI-related models for summary generation and task tracking.

```python
from django.db import models
from apps.blogs.models import Blog

class BlogSummary(models.Model):
    """AI-generated blog summaries"""
    
    blog = models.OneToOneField(
        Blog,
        on_delete=models.CASCADE,
        related_name='ai_summary'
    )
    
    summary = models.TextField()
    word_count = models.PositiveIntegerField(default=0)
    
    generated_by = models.CharField(
        max_length=50,
        choices=[
            ('openai', 'OpenAI GPT'),
            ('manual', 'Manual'),
        ],
        default='openai'
    )
    
    model_used = models.CharField(
        max_length=100,
        default='gpt-3.5-turbo'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Summary for: {self.blog.title}"
    
    def save(self, *args, **kwargs):
        # Auto-calculate word count
        self.word_count = len(self.summary.split())
        super().save(*args, **kwargs)


class AITask(models.Model):
    """Track AI processing tasks"""
    
    TASK_TYPES = (
        ('summarize', 'Summarize Blog'),
        ('rephrase', 'Rephrase Text'),
        ('generate_tags', 'Generate Tags'),
    )
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='ai_tasks'
    )
    
    task_type = models.CharField(
        max_length=50,
        choices=TASK_TYPES
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    
    result = models.JSONField(null=True, blank=True)
    error = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.task_type} for {self.blog.title} - {self.status}"
```

---

### **6. apps/ai_service/service.py**

**Purpose:** OpenAI API integration logic.

```python
import openai
from django.conf import settings
from .models import BlogSummary, AITask

# Configure OpenAI
openai.api_key = settings.OPENAI_API_KEY


class OpenAIService:
    """Service class for OpenAI API interactions"""
    
    @staticmethod
    def generate_blog_summary(blog_content, max_words=150):
        """
        Generate a summary of blog content using GPT.
        
        Args:
            blog_content (str): The full blog content
            max_words (int): Maximum words in summary
        
        Returns:
            str: AI-generated summary
        """
        try:
            prompt = f"Summarize the following blog post in {max_words} words:\n\n{blog_content}"
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional blog editor who creates concise, engaging summaries."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=300
            )
            
            summary = response.choices[0].message.content.strip()
            return summary
            
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")
    
    @staticmethod
    def rephrase_text(text, tone='professional'):
        """Rephrase text with specified tone"""
        try:
            prompt = f"Rephrase the following text in a {tone} tone:\n\n{text}"
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=500
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")
```

**Key Functions:**
- `generate_blog_summary()`: Creates AI summaries
- `rephrase_text()`: Rephrases content with different tones
- Error handling for API failures
- Configurable parameters (model, temperature, max_tokens)

---

## ⚛️ **React Frontend Structure**

### **Directory Overview**

```
frontend/
│
├── public/                     # Static public assets
│   ├── index.html             # HTML template
│   ├── favicon.ico
│   ├── logo192.png
│   └── manifest.json          # PWA manifest
│
├── src/                        # Source code
│   │
│   ├── components/             # Reusable components
│   │   ├── Navbar.js          # Navigation bar
│   │   ├── Footer.js          # Footer component
│   │   ├── BlogCard.js        # Blog preview card
│   │   ├── CommentSection.js  # Comments display
│   │   ├── LoadingSpinner.js  # Loading indicator
│   │   └── ProtectedRoute.js  # Route protection HOC
│   │
│   ├── pages/                  # Page components (routes)
│   │   ├── Home.js            # Landing page
│   │   ├── Login.js           # Login page
│   │   ├── Register.js        # Registration page
│   │   ├── BlogList.js        # Blog listing page
│   │   ├── BlogDetail.js      # Single blog view
│   │   ├── BlogEditor.js      # Create/Edit blog
│   │   ├── AdminDashboard.js  # Admin panel
│   │   ├── UserDashboard.js   # User dashboard
│   │   └── Profile.js         # User profile
│   │
│   ├── hooks/                  # Custom React hooks
│   │   ├── useAuth.js         # Authentication hook
│   │   ├── useBlog.js         # Blog operations hook
│   │   └── useDebounce.js     # Debounce hook
│   │
│   ├── utils/                  # Utility functions
│   │   ├── formatDate.js      # Date formatting
│   │   ├── truncateText.js    # Text utilities
│   │   └── validators.js      # Form validation
│   │
│   ├── api.js                  # Axios HTTP client
│   ├── store.js               # Zustand state management
│   ├── App.js                 # Main app component
│   ├── index.js               # Entry point
│   └── index.css              # Global styles
│
├── package.json                # npm dependencies
├── tailwind.config.js         # Tailwind configuration
├── postcss.config.js          # PostCSS configuration
└── .env                       # Environment variables
```

---

## 📄 **Frontend File Explanations**

### **1. src/api.js**

**Purpose:** Centralized HTTP client with automatic JWT handling.

```javascript
import axios from 'axios';

// Create axios instance
const api = axios.create({
  baseURL: 'http://localhost:8000/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor - Add JWT token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor - Handle token refresh
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // If 401 and not already retried
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        const refreshToken = localStorage.getItem('refresh_token');
        const response = await axios.post(
          'http://localhost:8000/api/auth/token/refresh/',
          { refresh: refreshToken }
        );

        const { access } = response.data;
        localStorage.setItem('access_token', access);

        // Retry original request with new token
        originalRequest.headers.Authorization = `Bearer ${access}`;
        return api(originalRequest);
      } catch (refreshError) {
        // Refresh failed - logout user
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        window.location.href = '/login';
        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  }
);

export default api;
```

**Why It's Critical:**
- Automatically adds JWT to all requests
- Handles token refresh on 401 errors
- Retries failed requests after refresh
- Logs out user if refresh fails

---

### **2. src/store.js**

**Purpose:** Global state management with Zustand.

```javascript
import { create } from 'zustand';
import api from './api';

const useBlogStore = create((set, get) => ({
  // State
  user: null,
  isAuthenticated: false,
  blogs: [],
  currentBlog: null,
  isLoading: false,
  errors: null,

  // Authentication Actions
  login: async (credentials) => {
    set({ isLoading: true, errors: null });
    try {
      const response = await api.post('/auth/login/', credentials);
      const { access, refresh, user } = response.data;
      
      // Store tokens
      localStorage.setItem('access_token', access);
      localStorage.setItem('refresh_token', refresh);
      
      set({
        user,
        isAuthenticated: true,
        isLoading: false,
      });
      
      return true;
    } catch (error) {
      set({
        errors: error.response?.data || 'Login failed',
        isLoading: false,
      });
      return false;
    }
  },

  logout: () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    set({
      user: null,
      isAuthenticated: false,
      blogs: [],
      currentBlog: null,
    });
  },

  // Blog Actions
  fetchBlogs: async (filters = {}) => {
    set({ isLoading: true });
    try {
      const response = await api.get('/blogs/', { params: filters });
      
      // Handle both array and paginated responses
      const blogsData = Array.isArray(response.data)
        ? response.data
        : response.data.results || [];
      
      set({
        blogs: blogsData,
        isLoading: false,
      });
    } catch (error) {
      set({
        errors: error.response?.data || 'Failed to fetch blogs',
        isLoading: false,
      });
    }
  },

  createBlog: async (blogData) => {
    set({ isLoading: true, errors: null });
    try {
      const response = await api.post('/blogs/', blogData);
      set((state) => ({
        blogs: [response.data, ...state.blogs],
        isLoading: false,
      }));
      return response.data;
    } catch (error) {
      set({
        errors: error.response?.data || 'Failed to create blog',
        isLoading: false,
      });
      throw error;
    }
  },

  updateBlog: async (id, blogData) => {
    set({ isLoading: true, errors: null });
    try {
      const response = await api.put(`/blogs/${id}/`, blogData);
      set((state) => ({
        blogs: state.blogs.map((blog) =>
          blog.id === id ? response.data : blog
        ),
        currentBlog: response.data,
        isLoading: false,
      }));
      return response.data;
    } catch (error) {
      set({
        errors: error.response?.data || 'Failed to update blog',
        isLoading: false,
      });
      throw error;
    }
  },

  deleteBlog: async (id) => {
    set({ isLoading: true });
    try {
      await api.delete(`/blogs/${id}/`);
      set((state) => ({
        blogs: state.blogs.filter((blog) => blog.id !== id),
        isLoading: false,
      }));
    } catch (error) {
      set({
        errors: error.response?.data || 'Failed to delete blog',
        isLoading: false,
      });
    }
  },

  // AI Actions
  generateSummary: async (blogId) => {
    set({ isLoading: true, errors: null });
    try {
      const response = await api.post(`/ai/generate-summary/`, {
        blog_id: blogId,
      });
      return response.data.summary;
    } catch (error) {
      set({
        errors: error.response?.data || 'Failed to generate summary',
        isLoading: false,
      });
      throw error;
    }
  },
}));

export default useBlogStore;
```

**Key Features:**
- Centralized state management
- Actions for authentication, blogs, AI
- Error handling
- Loading states
- LocalStorage integration

---

### **3. src/pages/BlogEditor.js**

**Purpose:** Create and edit blog posts with AI integration.

```javascript
import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { toast } from 'react-toastify';
import useBlogStore from '../store';

const BlogEditor = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const { createBlog, updateBlog, generateSummary, isLoading } = useBlogStore();
  
  const [formData, setFormData] = useState({
    title: '',
    content: '',
    category: '',
    tags: [],
    status: 'draft',
  });
  
  const [aiSummary, setAiSummary] = useState('');
  const [isGeneratingSummary, setIsGeneratingSummary] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleGenerateSummary = async () => {
    if (!formData.content) {
      toast.error('Please write some content first');
      return;
    }

    setIsGeneratingSummary(true);
    try {
      const summary = await generateSummary(id || 'temp');
      setAiSummary(summary);
      toast.success('Summary generated successfully!');
    } catch (error) {
      toast.error('Failed to generate summary');
    } finally {
      setIsGeneratingSummary(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      if (id) {
        // Update existing blog
        await updateBlog(id, formData);
        toast.success('Blog updated successfully!');
      } else {
        // Create new blog
        await createBlog(formData);
        toast.success('Blog created successfully!');
      }
      navigate('/dashboard');
    } catch (error) {
      toast.error('Failed to save blog');
    }
  };

  return (
    <div className="max-w-4xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">
        {id ? 'Edit Blog' : 'Create New Blog'}
      </h1>

      <form onSubmit={handleSubmit}>
        {/* Title */}
        <div className="mb-4">
          <label className="block text-sm font-medium mb-2">
            Title
          </label>
          <input
            type="text"
            name="title"
            value={formData.title}
            onChange={handleChange}
            className="w-full p-3 border rounded-lg"
            required
          />
        </div>

        {/* Content */}
        <div className="mb-4">
          <label className="block text-sm font-medium mb-2">
            Content
          </label>
          <textarea
            name="content"
            value={formData.content}
            onChange={handleChange}
            rows="15"
            className="w-full p-3 border rounded-lg"
            required
          />
        </div>

        {/* AI Summary Button */}
        <button
          type="button"
          onClick={handleGenerateSummary}
          disabled={isGeneratingSummary}
          className="mb-4 px-6 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700"
        >
          {isGeneratingSummary ? (
            <>🤖 Generating Summary...</>
          ) : (
            <>🤖 Generate AI Summary</>
          )}
        </button>

        {/* Display AI Summary */}
        {aiSummary && (
          <div className="mb-4 p-4 bg-blue-50 border border-blue-200 rounded-lg">
            <h3 className="font-semibold mb-2">AI-Generated Summary:</h3>
            <p>{aiSummary}</p>
          </div>
        )}

        {/* Submit Buttons */}
        <div className="flex gap-4">
          <button
            type="submit"
            name="status"
            value="draft"
            onClick={(e) => {
              setFormData({ ...formData, status: 'draft' });
            }}
            className="px-6 py-2 bg-gray-600 text-white rounded-lg"
          >
            Save Draft
          </button>
          
          <button
            type="submit"
            name="status"
            value="published"
            onClick={(e) => {
              setFormData({ ...formData, status: 'published' });
            }}
            className="px-6 py-2 bg-green-600 text-white rounded-lg"
          >
            Publish Now
          </button>
        </div>
      </form>
    </div>
  );
};

export default BlogEditor;
```

**Component Features:**
- Form state management
- AI summary generation
- Draft/Publish options
- Edit existing blogs
- Toast notifications
- Tailwind CSS styling

---

## 🔗 **How Components Connect**

```
User clicks "Create Blog"
      │
      ▼
BlogEditor.js component renders
      │
      ▼
User fills form and clicks "Generate Summary"
      │
      ▼
BlogEditor calls useBlogStore().generateSummary()
      │
      ▼
Zustand action makes API call via api.js
      │
      ▼
api.js adds JWT token from localStorage
      │
      ▼
Request sent to Django backend /api/ai/generate-summary/
      │
      ▼
Django view calls OpenAIService.generate_blog_summary()
      │
      ▼
OpenAI API processes and returns summary
      │
      ▼
Django saves to BlogSummary model
      │
      ▼
Response sent back to frontend
      │
      ▼
Zustand updates state
      │
      ▼
BlogEditor displays summary in UI
      │
      ▼
User clicks "Publish"
      │
      ▼
BlogEditor calls useBlogStore().createBlog()
      │
      ▼
Blog saved to database
      │
      ▼
User redirected to dashboard
```

---

## 🎨 **Styling Architecture**

### **Tailwind CSS Configuration**

```javascript
// tailwind.config.js
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#3B82F6',
        secondary: '#8B5CF6',
        accent: '#EC4899',
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
```

**Utility-First Approach:**
```jsx
// Instead of custom CSS
<div className="max-w-4xl mx-auto p-6 bg-white rounded-lg shadow-md">
  <h1 className="text-3xl font-bold text-gray-900 mb-4">
    Welcome
  </h1>
  <button className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition">
    Click Me
  </button>
</div>
```

---

## 🧪 **Testing Structure**

```
backend/
├── apps/
│   ├── users/
│   │   └── tests/
│   │       ├── test_models.py
│   │       ├── test_serializers.py
│   │       └── test_views.py
│   │
│   └── blogs/
│       └── tests/
│           ├── test_models.py
│           └── test_api.py

frontend/
└── src/
    ├── components/
    │   └── __tests__/
    │       ├── Navbar.test.js
    │       └── BlogCard.test.js
    │
    └── pages/
        └── __tests__/
            └── BlogList.test.js
```

---

This comprehensive guide provides complete understanding of how the codebase is organized! 🚀
