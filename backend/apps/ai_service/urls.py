from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AITaskViewSet

router = DefaultRouter()
router.register(r'tasks', AITaskViewSet, basename='ai-task')

urlpatterns = [
    path('', include(router.urls)),
]
