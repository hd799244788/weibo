#coding:utf8
from django.conf.urls import patterns,  include, url
from django.contrib import admin
from follow_the_girl import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^login/', views.usr_login),
	url(r'^search/', views.search),
	url(r'^find/', views.find),
	url(r'^register/', views.register),
	url(r'^logout/', views.user_logout),
]