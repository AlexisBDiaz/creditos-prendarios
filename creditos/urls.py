
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include 

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/', include('apps.usuario.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
