from django.shortcuts import render

from .forms import TaskForm
from .models import Task

# Create your views here.


def home(request):
    return render(request, 'task_controller/home.html', {})


def add_task(request):
    if request.method == "GET":
        form = TaskForm()
    else:
        form = TaskForm(data=request.POST)

        if form.is_valid():
            task = form.save(commit=False)

            if task is not None:
                task.task_user = request.user
                task.save()
                form = TaskForm()

    context = {'form': form}
    return render(request, 'task_controller/add_task.html', context)


def view_tasks(request):
    tasks = Task.objects.filter(task_user=request.user)

    priority_dict = {'H': 'High', 'M': 'Medium', 'L': 'Low'}
    status_dict = {'P': 'Pending', 'I': 'In Progress', 'C': 'Completed'}

    context = {'tasks': tasks, 'priority_dict': priority_dict, 'status_dict': status_dict}
    return render(request, 'task_controller/view_tasks.html', context)
