from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .forms import StudentRegistation
from .models import User
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import FormView




class Crud_view(View):
    registation = StudentRegistation
    template_name = 'cbv.html'
    def get(self, request, *args, **kwargs):

    
        registation = self.registation()
        user_data = User.objects.all()
        context={
         'registation':registation,
         'users': user_data,
        }
        return render(request, self.template_name,context)
    
    def post(self, request, *args, **kwargs):
        registation = self.registation(request.POST)
        if registation.is_valid():
           registation.save()
           return HttpResponse("Success")



# just TemplateView----------------------------------
class Home_view(TemplateView):
    template_name = 'home.html'


#TemplateView with data pass-----------------------------------
class Home_view_data(TemplateView):
    template_name = 'temdata.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg']="welcome to our website"
        return context


