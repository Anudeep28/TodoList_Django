from django.shortcuts import render, redirect
from .models import TaskModel



# Create your views here.
def addTask(request):
    task = request.POST['task']
    TaskModel.objects.create(task=task)
    return redirect('home')