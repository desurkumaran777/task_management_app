from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-task/', views.add_task, name='add-task'),
    path('view-tasks/', views.view_tasks, name='view-tasks'),
    path('view-task/<int:task_id>/', views.view_task, name='view-task'),
    path('edit-task/<int:task_id>/', views.edit_task, name='edit-task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete-task'),
]
