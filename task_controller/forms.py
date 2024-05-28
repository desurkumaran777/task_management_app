from django.forms import ModelForm
from django import forms

from .models import Task


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['task_title', 'task_desc', 'task_priority', 'task_status']
        labels = {
            'task_desc': 'Task description'
        }

        widgets = {
            'task_title': forms.TextInput(attrs={'class': 'form-control'}),
            'task_desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'task_priority': forms.Select(attrs={'class': 'form-control'}),
            'task_status': forms.Select(attrs={'class': 'form-control'}),
        }
