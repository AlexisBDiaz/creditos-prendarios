from django.conf.urls import url 

 
from django.urls import path, re_path
from django.conf.urls import include
#from django.contrib.auth.models import User

from apps.usuario import views

urlpatterns = [
    re_path(r'^user/$', views.UserList.as_view() ),
    re_path(r'^user/(?P<id>\d+)$', views.UserDetail.as_view() ),
]