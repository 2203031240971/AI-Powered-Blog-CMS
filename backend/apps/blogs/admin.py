from django.contrib import admin
from .models import Blog, Category, BlogSummary, Comment, Tag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'status', 'views_count', 'is_featured', 'published_at']
    list_filter = ['status', 'category', 'is_featured', 'created_at', 'published_at']
    search_fields = ['title', 'description', 'content']
    readonly_fields = ['views_count', 'created_at', 'updated_at', 'published_at']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Content', {'fields': ('title', 'slug', 'description', 'content', 'featured_image')}),
        ('Metadata', {'fields': ('author', 'category', 'status', 'is_featured')}),
        ('Statistics', {'fields': ('views_count', 'created_at', 'updated_at', 'published_at')}),
    )


@admin.register(BlogSummary)
class BlogSummaryAdmin(admin.ModelAdmin):
    list_display = ['blog', 'sentiment', 'generated_at']
    readonly_fields = ['generated_at', 'updated_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'blog', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'created_at']
    search_fields = ['author__username', 'content']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
