from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import StudentRegistation
from .models import User
from django.views.generic import TemplateView
from django.views.generic import FormView
print('hello')


#CRUD with CBV----------------------------------------------------------------
from django.views import View
class Crud_view(View):
    registation = StudentRegistation
    template_name = 'crud.html'
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
           print('hello')
           return redirect('/crud/')
    
class Delete_view(View): 
    def post(self,request, *args, **kwargs):
        pic_data = User.objects.get(id=self.kwargs['hi'])
        pic_data.delete()
        return redirect('/crud/')




class Edit_view(View):
    template_name = 'crud/update.html'
    def post(self, request, *args, **kwargs):
        pi = User.objects.get(id=self.kwargs['pk'])
        fm = StudentRegistation(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/crud/')
        context = {
         'edit_form': fm
         }
        
        return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        pi = User.objects.get(id=self.kwargs['pk'])
        fm = StudentRegistation(instance=pi)
        context = {
        'edit_form': fm
        }

        return render(request, self.template_name, context)


## FBV----------------------------------------------------------------------


## CRUD with FBV
# def crud(request):
#     templates = 'crud.html'
#     registation = StudentRegistation()
#     if request.method == 'POST':
#         register = StudentRegistation(request.POST)
#         if register.is_valid():
#             register.save()
#             return redirect('/crud/')
#     user_data = User.objects.all()
#     context = {
#         'registation': registation,
#         'users': user_data,
#     }

#     return render(request, template_name=templates, context=context)




# def delete(request, hi):
#     if request.method == "POST":
#         pic_data = User.objects.get(id=hi)
#         pic_data.delete()
#         return redirect('/crud/')





# def edit_data(request, pk):
#     templates = 'crud/update.html'
#     if request.method == "POST":
#         pi = User.objects.get(id=pk)
#         fm = StudentRegistation(request.POST, instance=pi)
#         if fm.is_valid():
#             fm.save()
#             return redirect('/crud/')
#     else:
#         pi = User.objects.get(id=pk)
#         fm = StudentRegistation(instance=pi)

#     context = {
#         'edit_form': fm
#     }
#     return render(request, template_name=templates, context=context)
