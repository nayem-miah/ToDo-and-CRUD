from . import views
from django.urls import path


urlpatterns = [

    ## for FBV
    # path('', views.crud, name='form'),
    # path('delete/<int:hi>/', views.delete, name='delete_data'),
    # path('edit_data/<int:pk>/', views.edit_data, name='edit_data'),


    #for CBV
    path('', views.Crud_view.as_view(), name='form'),
    path('delete/<int:hi>/', views.Delete_view.as_view(), name='delete_data'),
    path('edit_data/<int:pk>/', views.Edit_view.as_view(), name='edit_data'),

]
