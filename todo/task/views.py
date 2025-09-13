from django.shortcuts import render
from .models import Task

# Create your views here.
def task_list(request):
    status_filter = request.GET.get('status', all)

    category_filter = request.GET.get('category', all)
    tasks = Task.objects.filter(user = request.user)

    if status_filter != 'all':
        tasks = tasks.filter(is_completed = (status_filter == 'completed'))

    if category_filter != 'all':
        tasks = tasks.filter(category = category_filter)

    completed_tasks = tasks.filter(is_completed = True)
    pending_tasks = tasks.filter(is_completed = False)

    return render(request, '', {
        'completed_tasks' : completed_tasks,
        'pending_tasks' : pending_tasks,
        'status_filter' : status_filter,
        'category_filter' : category_filter
    })