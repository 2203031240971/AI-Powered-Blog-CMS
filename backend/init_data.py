"""
Initialize categories and tags for the blog CMS.
Run this script to populate the database with initial data.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.blogs.models import Category, Tag

# Create categories
categories = [
    {'name': 'Technology', 'description': 'Articles about technology, programming, and software development'},
    {'name': 'Business', 'description': 'Business strategies, entrepreneurship, and marketing'},
    {'name': 'Lifestyle', 'description': 'Lifestyle, health, wellness, and personal development'},
    {'name': 'Travel', 'description': 'Travel guides, tips, and destination reviews'},
    {'name': 'Food', 'description': 'Recipes, restaurant reviews, and culinary experiences'},
    {'name': 'Education', 'description': 'Learning resources, tutorials, and educational content'},
]

print("Creating categories...")
for cat_data in categories:
    category, created = Category.objects.get_or_create(
        name=cat_data['name'],
        defaults={'description': cat_data['description']}
    )
    status = "Created" if created else "Already exists"
    print(f"  {status}: {category.name}")

# Create common tags
tags = [
    'Python', 'JavaScript', 'Web Development', 'AI', 'Machine Learning',
    'Tutorial', 'Guide', 'Tips', 'News', 'Review',
    'Beginner', 'Advanced', 'Tips & Tricks', 'Best Practices',
    'Django', 'React', 'API', 'Database', 'Security',
    'Performance', 'Design', 'UX', 'Mobile', 'Cloud'
]

print("\nCreating tags...")
for tag_name in tags:
    tag, created = Tag.objects.get_or_create(name=tag_name)
    status = "Created" if created else "Already exists"
    print(f"  {status}: {tag.name}")

print("\n✅ Database initialization complete!")
print(f"Total categories: {Category.objects.count()}")
print(f"Total tags: {Tag.objects.count()}")
