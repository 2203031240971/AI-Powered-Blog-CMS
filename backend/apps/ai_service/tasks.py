from celery import shared_task
from django.utils import timezone
from apps.blogs.models import Blog, BlogSummary
from apps.ai_service.models import AITask
from apps.ai_service.service import AIService

@shared_task
def generate_blog_summary_task(blog_id):
    """Celery task to generate blog summary asynchronously."""
    try:
        blog = Blog.objects.get(id=blog_id)
        
        # Create AI task record
        task = AITask.objects.create(
            blog=blog,
            task_type='summarization',
            status=AITask.Status.PROCESSING
        )
        
        # Generate summary using AI service
        ai_service = AIService()
        result = ai_service.generate_complete_summary(blog)
        
        if result['status'] == 'success':
            # Update or create BlogSummary
            blog_summary, created = BlogSummary.objects.update_or_create(
                blog=blog,
                defaults={
                    'summary': result['summary'],
                    'key_points': result['key_points'],
                    'sentiment': result['sentiment']
                }
            )
            
            # Update task
            task.status = AITask.Status.COMPLETED
            task.result = result
            task.completed_at = timezone.now()
            task.save()
            
            return {'status': 'success', 'summary_id': blog_summary.id}
        else:
            # Task failed
            task.status = AITask.Status.FAILED
            task.error = result.get('message', 'Unknown error')
            task.completed_at = timezone.now()
            task.save()
            
            return {'status': 'error', 'message': result.get('message', 'Unknown error')}
    except Blog.DoesNotExist:
        return {'status': 'error', 'message': 'Blog not found'}
    except Exception as e:
        task.status = AITask.Status.FAILED
        task.error = str(e)
        task.completed_at = timezone.now()
        task.save()
        
        return {'status': 'error', 'message': str(e)}
