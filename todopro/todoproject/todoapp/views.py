from django.shortcuts import render, redirect
from .forms import todoform
from .models import task


# Create your views here.
def add(request):
    Task1 = task.objects.all()
    if request.method == "POST":
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date= request.POST.get('date','')
        Task = task(name=name, priority=priority,date=date)
        Task.save()
    return render(request, 'index.html',{'task': Task1})

def delete(request,id):
    task2= task.objects.get(id=id)
    if request.method =="POST":
        task2.delete()
        return redirect("/")
    return render(request,'delete.html')


def update(request,id):
    task3=task.objects.get(id=id)
    f=todoform(request.POST or None,instance=task3)
    if f.is_valid():
        f.save()
        return redirect("/")
    return render(request,'edit.html',{'f':f,'task':task3})