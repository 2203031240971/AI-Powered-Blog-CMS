from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.utils import timezone
from .models import Blog, Category, BlogSummary, Comment, Tag
from .serializers import (
    BlogListSerializer, BlogDetailSerializer, BlogCreateUpdateSerializer,
    CategorySerializer, CommentSerializer, TagSerializer, BlogSummarySerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for blog categories."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]


class BlogViewSet(viewsets.ModelViewSet):
    """ViewSet for blog posts with AI summarization."""
    queryset = Blog.objects.select_related('author', 'category').prefetch_related('tags', 'comments')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['status', 'category', 'author', 'is_featured']
    search_fields = ['title', 'description', 'content']
    ordering_fields = ['created_at', 'published_at', 'views_count']
    ordering = ['-published_at', '-created_at']
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BlogDetailSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return BlogCreateUpdateSerializer
        return BlogListSerializer
    
    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        blog = serializer.save(author=self.request.user)
        if blog.status == 'published':
            blog.published_at = timezone.now()
            blog.save()
    
    def perform_update(self, serializer):
        # Check if user is the author or admin
        blog = self.get_object()
        if blog.author != self.request.user and not self.request.user.is_staff:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You don't have permission to edit this blog.")
        
        blog = serializer.save()
        if blog.status == 'published' and not blog.published_at:
            blog.published_at = timezone.now()
            blog.save()
    
    def perform_destroy(self, instance):
        # Check if user is the author or admin
        if instance.author != self.request.user and not self.request.user.is_staff:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You don't have permission to delete this blog.")
        instance.delete()
    
    @action(detail=True, methods=['get'])
    def increment_views(self, request, pk=None):
        """Increment blog view count."""
        blog = self.get_object()
        blog.views_count += 1
        blog.save(update_fields=['views_count'])
        return Response({'views_count': blog.views_count})
    
    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def generate_summary(self, request, pk=None):
        """Generate AI summary for the blog post."""
        blog = self.get_object()
        from apps.ai_service.tasks import generate_blog_summary_task
        
        # Check if user has permission
        if blog.author != request.user and not request.user.is_staff:
            return Response(
                {'error': 'Permission denied'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Trigger background task
        generate_blog_summary_task.delay(blog.id)
        
        return Response({
            'status': 'Summary generation started',
            'blog_id': blog.id
        })
    
    @action(detail=True, methods=['post'])
    def comment(self, request, pk=None):
        """Add comment to blog post."""
        blog = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(blog=blog, author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        """Get approved comments for blog post."""
        blog = self.get_object()
        comments = blog.comments.filter(is_approved=True)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured blogs."""
        blogs = self.queryset.filter(is_featured=True, status='published')
        serializer = self.get_serializer(blogs, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def latest(self, request):
        """Get latest published blogs."""
        blogs = self.queryset.filter(status='published')[:5]
        serializer = self.get_serializer(blogs, many=True)
        return Response(serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    """ViewSet for blog tags."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    
    @action(detail=True, methods=['get'])
    def blogs(self, request, slug=None):
        """Get all blogs with this tag."""
        tag = self.get_object()
        blogs = tag.blogs.filter(status='published')
        serializer = BlogListSerializer(blogs, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for managing comments."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['blog', 'is_approved']
    ordering = ['-created_at']
    
    def get_permissions(self):
        if self.action in ['approve', 'reject', 'destroy']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def approve(self, request, pk=None):
        """Approve a comment."""
        comment = self.get_object()
        if comment.blog.author != request.user and not request.user.is_staff:
            return Response(
                {'error': 'Permission denied'},
                status=status.HTTP_403_FORBIDDEN
            )
        comment.is_approved = True
        comment.save()
        return Response({'status': 'comment approved'})
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def reject(self, request, pk=None):
        """Reject a comment."""
        comment = self.get_object()
        if comment.blog.author != request.user and not request.user.is_staff:
            return Response(
                {'error': 'Permission denied'},
                status=status.HTTP_403_FORBIDDEN
            )
        comment.is_approved = False
        comment.save()
        return Response({'status': 'comment rejected'})
