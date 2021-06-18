from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<pk>/', views.update_task, name='update_task'),
    path('delete_task/<pk>/', views.delete_task, name='delete_task'),
    path('test/<bk>/', views.test, name='test'),

]
