from django.urls import path
from . import views

urlpatterns = [

    path('<int:myid>/', views.show_data, name='show')

]
