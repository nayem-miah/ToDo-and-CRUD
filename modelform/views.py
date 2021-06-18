from django.shortcuts import render, redirect
from .form import Mmform
from django.http import HttpResponseRedirect


def modelform(request):
    submitted = False
    templates = 'modelform.html'
    mmform = Mmform()
    if request.method == 'POST':
        form = Mmform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/modelform?submitted')
    else:
        if 'submitted' in request.GET:
            submitted = True
    context = {
        'form': mmform,
        'submitted': submitted,
    }
    return render(request, template_name=templates, context=context)
