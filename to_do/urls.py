from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('to_do_index.urls')),
    path('form/', include('form.urls')),
    path('url/', include('dynamic_url.urls')),
    path('modelform/', include('modelform.urls')),
    path('auth/', include('auth_pass.urls')),
    path('crud/', include('crud.urls')),
    path('cbv/', include('CBV.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
