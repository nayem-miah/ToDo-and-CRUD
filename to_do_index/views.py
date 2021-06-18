from django.shortcuts import render, redirect
from .models import Task
from .forms import Taskform

def index(request):
    template = 'index.html'
    tasks = Task.objects.all() #for grabbong data from database to page
    blanked_form = Taskform() #for form showing
    if request.method == 'POST':
        form = Taskform(request.POST) # for grabbing data from the form to database
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'task_data': tasks, #for grabbong data from database to page
        'form': blanked_form, #for form showing
    }

    return render(request, template_name=template, context=context)


def update_task(request, pk):

    if request.method == 'POST':
        task = Task.objects.get(id=pk)
        update = Taskform(request.POST, instance=task)
        if update.is_valid():
            update.save()
            return redirect('/')
    else:
        task = Task.objects.get(id=pk)
        update = Taskform(instance=task)
    context = {
        'form': update
    }

    return render(request, 'task.html', context=context)

def delete_task(request, pk):

        pick = Task.objects.get(id=pk)
        pick.delete()
        return redirect('/')

def test(request, bk):

    context={'sk': bk}
    return render(request, 'test.html', context= context)