from rest_framework import serializers
from .models import AITask

class AITaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = AITask
        fields = ['id', 'blog', 'task_type', 'status', 'result', 'error', 
                  'created_at', 'updated_at', 'completed_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'completed_at']
