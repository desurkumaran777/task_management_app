from django.shortcuts import render

from .forms import TaskForm

# Create your views here.


def home(request):
    return render(request, 'task_controller/home.html', {})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(data=request.POST)

        if form.is_valid():
            task = form.save(commit=False)

            if task is not None:
                task.task_user = request.user
                task.save()
                
    return render(request, 'task_controller/add_task.html', context={})


def view_tasks(request):
    return render(request, 'task_controller/view_tasks.html', {})
