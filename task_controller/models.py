from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]

    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('I', 'In Progress'),
        ('C', 'Completed'),
    ]

    task_id = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length=255)
    task_desc = models.TextField()
    task_priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    task_status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    task_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title

    class Meta:
        db_table = 'task_tbl'


class TaskPriority(models.Model):
    PRIORITY_CHOICES = [
        ('A', 'All'),
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]

    task_priority = models.CharField(
        max_length=1, choices=PRIORITY_CHOICES, default='A')
    task_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.task_priority} - {self.task_user}"

    class Meta:
        db_table = 'task_priority_tbl'
        verbose_name_plural = 'Task Priorities'
