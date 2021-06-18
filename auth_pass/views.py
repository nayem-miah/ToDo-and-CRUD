from django.shortcuts import render
from .models import School, Student


def auth(request):
    templates = 'auth.html'
    student = Student.objects.all()
    context= {
        'student': student
    }
    return render(request, template_name=templates, context=context)
