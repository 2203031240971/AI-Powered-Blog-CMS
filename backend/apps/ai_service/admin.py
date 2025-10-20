from django.contrib import admin
from .models import AITask

@admin.register(AITask)
class AITaskAdmin(admin.ModelAdmin):
    list_display = ['blog', 'task_type', 'status', 'created_at', 'completed_at']
    list_filter = ['status', 'task_type', 'created_at']
    search_fields = ['blog__title']
    readonly_fields = ['created_at', 'updated_at', 'completed_at', 'result', 'error']
