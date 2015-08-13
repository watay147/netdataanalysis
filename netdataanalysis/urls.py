"""netdataanalysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','webpage.views.index',name='index'),

    url(r'^indexcreditorders$','webpage.views.indexcreditorders',name='indexcreditorders'),
    url(r'^indexevents$','webpage.views.indexevents',name='indexevents'),
    url(r'^indexnews$','webpage.views.indexnews',name='indexnews'),
    url(r'^indexattentions$','webpage.views.indexattentions',name='indexattentions'),
    url(r'^indexsearch/','webpage.views.indexsearch',name='indexsearch'),

    url(r'^viewcompany/(\d+)$','webpage.views.viewcompany',name='viewcompany'),
    url(r'^complotdata$','webpage.views.complotdata',name='complotdata'),
    url(r'^eventstipslist','webpage.views.eventstipslist',name='eventstipslist'),
    url(r'^comintro/(\d+)$','webpage.views.comintro',name='comintro'),
    url(r'^comfinance/(\d+)$','webpage.views.comfinance',name='comfinance'),

    url(r'^viewevent/(\d+)$','webpage.views.viewevent',name='viewevent'),
    url(r'^viewevent/','webpage.views.viewevent',name='Dviewevent'),
    

    url(r'^viewnew/(\d+)$','webpage.views.viewnew',name='viewnew'),

]
