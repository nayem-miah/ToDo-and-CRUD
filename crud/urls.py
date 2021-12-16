from . import views
from django.urls import path


urlpatterns = [
    
    ## for FBV
    # path('', views.crud, name='form'),

    #for CBV
    path('', views.Crud_view.as_view(), name='form'),

    path('delete/<int:hi>/', views.delete, name='delete_data'),
    path('edit_data/<int:pk>/', views.edit_data, name='edit_data'),
]
