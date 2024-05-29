from django.shortcuts import render, redirect

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

    context = {'tasks': tasks, 'priority_dict': priority_dict,
               'status_dict': status_dict}
    return render(request, 'task_controller/view_tasks.html', context)


def view_task(request, task_id):
    task = Task.objects.get(task_id=task_id)

    form = TaskForm()
    form.initial['task_title'] = task.task_title
    form.initial['task_desc'] = task.task_desc
    form.initial['task_priority'] = task.task_priority
    form.initial['task_status'] = task.task_status

    form.fields['task_title'].disabled = True
    form.fields['task_desc'].disabled = True
    form.fields['task_priority'].disabled = True
    form.fields['task_status'].disabled = True

    context = {'form': form, 'task': task}

    return render(request, 'task_controller/view_task.html', context)


def edit_task(request, task_id):
    task = Task.objects.get(task_id=task_id)

    if request.method == "GET":
        form = TaskForm()
        form.initial['task_title'] = task.task_title
        form.initial['task_desc'] = task.task_desc
        form.initial['task_priority'] = task.task_priority
        form.initial['task_status'] = task.task_status

        context = {'form': form, 'task': task}

        return render(request, 'task_controller/edit_task.html', context)
    else:
        task.task_title = request.POST['task_title']
        task.task_desc = request.POST['task_desc']
        task.task_priority = request.POST['task_priority']
        task.task_status = request.POST['task_status']

        task.save()

        return redirect('view-tasks')


def delete_task(request, task_id):
    task = Task.objects.get(task_id=task_id)
    task.delete()
    return redirect('view-tasks')
