from rest_framework import serializers
from .models import Blog, Category, BlogSummary, Comment, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']
        read_only_fields = ['id']


class BlogSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogSummary
        fields = ['id', 'summary', 'key_points', 'sentiment', 'generated_at', 'updated_at']
        read_only_fields = ['id', 'generated_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'is_approved', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at', 'is_approved']


class BlogListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'description', 'featured_image', 'author', 
                  'category', 'tags', 'status', 'views_count', 'is_featured', 'created_at', 'published_at']
        read_only_fields = ['id', 'slug', 'created_at']


class BlogDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True, required=False)
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    ai_summary = BlogSummarySerializer(source='ai_summary_record', read_only=True)
    
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'description', 'content', 'featured_image',
                  'author', 'category', 'category_id', 'tags', 'status', 'views_count',
                  'is_featured', 'comments', 'ai_summary', 'created_at', 'updated_at', 'published_at']
        read_only_fields = ['id', 'slug', 'author', 'views_count', 'created_at', 'updated_at']


class BlogCreateUpdateSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(required=False, allow_null=True)
    tag_ids = serializers.ListField(
        child=serializers.IntegerField(),
        required=False,
        allow_empty=True
    )
    
    class Meta:
        model = Blog
        fields = ['title', 'description', 'content', 'featured_image', 
                  'category_id', 'tag_ids', 'status', 'is_featured']
    
    def to_internal_value(self, data):
        import json
        from django.http import QueryDict
        
        # Make data mutable if it's a QueryDict
        if isinstance(data, QueryDict):
            data = data.copy()
        elif hasattr(data, '_mutable') and not data._mutable:
            data._mutable = True
        
        # Handle tag_ids if it comes as a JSON string (from FormData)
        if 'tag_ids' in data:
            tag_ids_value = data.get('tag_ids')
            
            # If it's a string, try to parse it as JSON
            if isinstance(tag_ids_value, str) and tag_ids_value:
                try:
                    parsed_tags = json.loads(tag_ids_value)
                    # Ensure it's a list of integers
                    if isinstance(parsed_tags, list):
                        data['tag_ids'] = [int(tag_id) for tag_id in parsed_tags if isinstance(tag_id, (int, str)) and str(tag_id).isdigit()]
                    else:
                        data['tag_ids'] = []
                except (json.JSONDecodeError, ValueError, TypeError) as e:
                    print(f"Error parsing tag_ids: {e}, value: {tag_ids_value}")
                    data['tag_ids'] = []
            # If it's already a list, use it directly
            elif isinstance(tag_ids_value, list):
                data['tag_ids'] = [int(tag_id) for tag_id in tag_ids_value if isinstance(tag_id, (int, str)) and str(tag_id).isdigit()]
            # If it's None or empty, set empty list
            elif not tag_ids_value:
                data['tag_ids'] = []
        
        return super().to_internal_value(data)
    
    def create(self, validated_data):
        category_id = validated_data.pop('category_id', None)
        tag_ids = validated_data.pop('tag_ids', [])
        validated_data['author'] = self.context['request'].user
        
        blog = Blog.objects.create(**validated_data)
        
        if category_id:
            blog.category_id = category_id
            blog.save()
        
        if tag_ids:
            blog.tags.set(tag_ids)
        
        return blog
    
    def update(self, instance, validated_data):
        category_id = validated_data.pop('category_id', None)
        tag_ids = validated_data.pop('tag_ids', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if category_id is not None:
            instance.category_id = category_id
        
        if tag_ids is not None:
            instance.tags.set(tag_ids)
        
        instance.save()
        return instance
