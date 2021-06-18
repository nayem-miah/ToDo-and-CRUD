from django.shortcuts import render, redirect
from .forms import StudentRegistation
from .models import User

def crud(request):
    templates = 'crud.html'
    registation = StudentRegistation()
    if request.method == 'POST':
        register = StudentRegistation(request.POST)
        if register.is_valid():
            register.save()
            return redirect('/crud/')
    user_data = User.objects.all()
    context = {
        'registation': registation,
        'users': user_data,
    }

    return render(request, template_name=templates, context=context)


def delete(request, hi):
    if request.method == "POST":
        pic_data = User.objects.get(id=hi)
        print(pic_data)
        pic_data.delete()
        return redirect('/crud/')


def edit_data(request, pk):
    templates = 'crud/update.html'
    if request.method == "POST":
        pi = User.objects.get(id=pk)
        fm = StudentRegistation(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/crud/')
    else:
        pi = User.objects.get(id=pk)
        fm = StudentRegistation(instance=pi)

    context = {
        'edit_form': fm
    }
    return render(request, template_name=templates, context=context)
