from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import AITask
from .serializers import AITaskSerializer

class AITaskViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for viewing AI tasks."""
    queryset = AITask.objects.all()
    serializer_class = AITaskSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['blog', 'status', 'task_type']
    ordering = ['-created_at']
    
    @action(detail=False, methods=['get'])
    def pending(self, request):
        """Get pending AI tasks."""
        tasks = self.queryset.filter(status=AITask.Status.PENDING)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def failed(self, request):
        """Get failed AI tasks."""
        tasks = self.queryset.filter(status=AITask.Status.FAILED)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)
