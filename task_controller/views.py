from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import TaskForm, TaskPriorityForm
from .models import Task, TaskPriority

# Create your views here.


def home(request):
    return render(request, 'task_controller/home.html', {})


@login_required
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


@login_required
def view_tasks(request):
    if request.method == "GET":
        tasks = Task.objects.filter(task_user=request.user)
        form = TaskPriorityForm()
    else:
        if TaskPriority.objects.filter(task_user=request.user).exists():
            selected_task_priority = get_object_or_404(
                TaskPriority, task_user=request.user)
            selected_task_priority.task_priority = request.POST['task_priority']
            selected_task_priority.save()
            form = TaskPriorityForm()
            form.initial['task_priority'] = request.POST['task_priority']
            selected_task_priority = selected_task_priority.task_priority
        else:
            form = TaskPriorityForm(data=request.POST)
            if form.is_valid():
                task_priority = form.save(commit=False)
                if task_priority is not None:
                    task_priority.task_user = request.user
                    task_priority.save()
                    selected_task_priority = request.POST['task_priority']

        if selected_task_priority == 'A':
            tasks = Task.objects.filter(task_user=request.user)
        else:
            tasks = Task.objects.filter(
                task_user=request.user, task_priority=selected_task_priority)

    priority_dict = {'H': 'High', 'M': 'Medium', 'L': 'Low'}
    status_dict = {'P': 'Pending', 'I': 'In Progress', 'C': 'Completed'}

    context = {'tasks': tasks, 'priority_dict': priority_dict,
               'status_dict': status_dict, 'form': form}
    return render(request, 'task_controller/view_tasks.html', context)


@login_required
def view_task(request, task_id):
    task = get_object_or_404(Task, task_id=task_id)

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


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, task_id=task_id)

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


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, task_id=task_id)
    task.delete()
    return redirect('view-tasks')
