from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-task', views.add_task, name='add-task'),
    path('view-tasks', views.view_tasks, name='view-tasks'),
]
