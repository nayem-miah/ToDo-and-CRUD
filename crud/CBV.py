



# #for CBV
# path('', views.Crud_view.as_view(), name='form'),


# #CRUD with CBV
# from django.views import View
# class Crud_view(View):
#     registation = StudentRegistation
#     template_name = 'crud.html'
#     def get(self, request, *args, **kwargs):

    
#         registation = self.registation()
#         user_data = User.objects.all()
#         context={
#          'registation':registation,
#          'users': user_data,
#         }
#         return render(request, self.template_name,context)
    
#     def post(self, request, *args, **kwargs):
#         registation = self.registation(request.POST)
#         if registation.is_valid():
#            registation.save()
#            return HttpResponse("Success")



## ----------------------------------------------------------------------
##---------------------------Template_view------------------------------


# from django.views.generic import TemplateView
# class Home_view(TemplateView):
#     template_name = 'home.html'




# # ------------------------Template_view without views.py---------------------
# from django.views.generic import TemplateView
# path('',TemplateView.as_view(template_name = 'home.html'), name='homeview'),



# # ------------------------Template_view with data pass------------------------


# class Home_view(TemplateView):
#     template_name = 'home.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['msg']="welcome to our website"
#         return context





## ----------------------------------------------------------------------
##---------------------------form_view-----------------------------------


from django.views.generic import FormView
