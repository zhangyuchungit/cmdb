from django.conf.urls import patterns, include, url
from django.contrib import admin
from app04 import views
urlpatterns = patterns('',

   url(r'^ajax/$', views.Ajax),
   url(r'^add/$', views.Add),
   url(r'^userlist/$', views.Userlist),
   url(r'^update/$', views.Update),
   url(r'^chouti/$', views.ChouTi),
   url(r'^index/$', views.Index),
   url(r'^login/$', views.Login),
   url(r'^register/$', views.Register),
   url(r'^upload/$', views.UpLoad),
   url(r'^svnupload/$', views.SvnupLoad),
   url(r'^tar/$', views.Tar),
   url(r'^loaddir/$', views.LoadDir),
   
)
