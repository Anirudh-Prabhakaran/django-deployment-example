from django.conf.urls import url
from AimbaalWebApp import views

app_name = 'AimbaalWebApp'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
