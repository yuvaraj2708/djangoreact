from django.urls import path
from . import views

urlpatterns = [
    path('api/tasks/', views.TaskList.as_view(), name='task-list'),
    # Add URL patterns for other views here
]