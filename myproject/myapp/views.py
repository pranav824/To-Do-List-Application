from django.shortcuts import render, redirect
from .models import Task
from django.urls import reverse
# Create your views here.
def index(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'myapp/index.html', context)

def add(request):
    if request.method == "POST":
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('myapp:index')
    return render(request, 'myapp/index.html')

def complete(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = True
    task.save()
    return redirect('myapp:index')

def delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('myapp:index')

def update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        task.title = request.POST['title']
        task.save()
        return redirect(reverse('myapp:index'))
    context = {'task': task}
    return render(request, 'myapp/update.html', context)