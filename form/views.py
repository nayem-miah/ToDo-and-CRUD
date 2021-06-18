from django.shortcuts import render
from . import forms


def form(request):
    first_model = forms.Mform1
    context = {
        'form_pass': first_model
    }

    template='form.html'
    return render(request, template_name=template, context=context)
