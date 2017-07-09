from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'portal'

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    #url(r'^login/$', views.loginpage),
    url(r'^redirect/$', views.redirect, name='redirect'),
    url(r'^vmlist/$', views.vmlist, name='vmlist'),
    url(r'^deploy/$', views.deploy, name='deploy'),
    url(
        r'^login/$', 
        auth_views.login, 
        { 'template_name': 'portal/login.html' },
        name='login'
    ),
    url(
        r'^logout/$', 
        auth_views.logout, 
        { 'template_name': 'portal/logout.html' },
        name='logout'
    ),
]
