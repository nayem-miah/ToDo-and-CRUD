from . import views
from django.urls import path


urlpatterns = [
    path('', views.crud, name='form'),
    path('delete/<int:hi>/', views.delete, name='delete_data'),
    path('edit_data/<int:pk>/', views.edit_data, name='edit_data'),
]
