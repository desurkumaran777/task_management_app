from django.contrib import admin
from .models import Task, TaskPriority

# Register your models here.

admin.site.register(Task)
admin.site.register(TaskPriority)