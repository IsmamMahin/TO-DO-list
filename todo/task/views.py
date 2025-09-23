from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def task_list(request):
    status_filter = request.GET.get('status', 'all')

    category_filter = request.GET.get('category', 'all')
    tasks = Task.objects.filter(user = request.user)

    if status_filter != 'all':
        tasks = tasks.filter(is_completed = (status_filter == 'completed'))

    if category_filter != 'all':
        tasks = tasks.filter(category = category_filter)

    completed_tasks = tasks.filter(is_completed = True)
    pending_tasks = tasks.filter(is_completed = False)

    return render(request, 'task_list.html', {
        'completed_tasks' : completed_tasks,
        'pending_tasks' : pending_tasks,
        'status_filter' : status_filter,
        'category_filter' : category_filter
    })

#task create
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False) #Ready to save but not actually saves
            task.user = request.user
            task.save() # database e save hobe
            return redirect('task_list')
    else:
            form = TaskForm()
    return render(request, 'task_form.html', {'form' : form})
    
# Task Detail Page
@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    return render(request, 'task_detail.html', {'task' : task})

# Task Delete Page
@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')

# Mark task as completed
@login_required
def task_mark_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.is_completed = True
    task.save()
    return redirect('task_list')

# User register
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username = username, password = password)
#             login(user)
#             return redirect('task_list')
#     else:
#         form = UserCreationForm()

#     return render(request, 'register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the form to create the user and get the user object.
            user = form.save()
            
            # Use the correct login function call, passing both request and user.
            login(request, user)
            
            # Redirect to the desired page after successful registration and login.
            return redirect('task_list')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})