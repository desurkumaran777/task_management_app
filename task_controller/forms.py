from django.forms import ModelForm

from .models import Task


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['task_title', 'task_desc', 'task_priority', 'task_status']
