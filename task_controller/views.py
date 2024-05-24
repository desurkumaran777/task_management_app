from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'task_controller/home.html', {})


def add_task(request):
    return render(request, 'task_controller/add_task.html', {})


def view_tasks(request):
    return render(request, 'task_controller/view_tasks.html', {})
