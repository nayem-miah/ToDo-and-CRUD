from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
  
  path('', views.Crud_view.as_view(), name='cbv'),
  path('home/',views.Home_view.as_view(), name='home'),
  path('temdata/',views.Home_view_data.as_view(), name='temdata'),

  # TemplateView without views.py
  path('temp/', TemplateView.as_view(template_name = 'temp.html'), name='temp'), 
 
]
