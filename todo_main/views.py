from django.http import HttpResponse
from django.shortcuts import render
from todo_app.models import TaskModel


def home(request):
    
    tasks = TaskModel.objects.filter(is_completed=False).order_by('-updated_at')
    completed_tasks = TaskModel.objects.filter(is_completed=True).order_by('-updated_at')
    
    context={
        'tasks': tasks,
        "completed_tasks": completed_tasks
        }
    return render(request, 'home.html', context)