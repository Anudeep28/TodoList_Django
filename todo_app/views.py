from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel



# Create your views here.
def addTask(request):
    task = request.POST['task']
    TaskModel.objects.create(task=task)
    return redirect('home')


def doneTask(request, pk):
    #task = TaskModel.objects.get(pk=pk)
    task = get_object_or_404(TaskModel,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def undoTask(request, pk):
    #task = TaskModel.objects.get(pk=pk)
    task = get_object_or_404(TaskModel, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def editTask(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)

    if request.method == 'POST':
        task.task = request.POST['task']
        task.save()
        return redirect('home')
    else:
        context = {
            "task":task
        }
        return render(request, 'editTask.html', context)

def deleteTask(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    task.delete()
    return redirect('home')
