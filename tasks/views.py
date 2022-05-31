from django.shortcuts import render,redirect
from .models import Task
# Create your views here.
def list_tasks(request):
    tasks=Task.objects.all()
    return render(request, 'list_tasks.html',{'tasks':tasks})
def create_task(request):
    task=Task(title=request.POST['task-name'], description=request.POST['task-description'])
    task.save()
    print(request.POST)
    return redirect('/tasks/')

def delete_task(request,task_id):
    task=Task.objects.get(id=task_id)
    task.delete()
    print(request.POST)
    print(task_id)
    return redirect('/tasks/')