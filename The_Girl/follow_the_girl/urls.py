#coding:utf8
from django.conf.urls import patterns,  include, url
from django.contrib import admin
from follow_the_girl import views

urlpatterns = [
	url(r'^index/', views.index),
	url(r'^$', views.usr_login),
	url(r'^test', views.save),
	url(r'^save_id', views.save_id),
	url(r'^weibo/', views.weibo),
	url(r'^yuanchuang/', views.yuanchuang),
	url(r'^tupian/', views.tupian),
	url(r'^weibo/', views.weibo),
	url(r'^search/', views.search),
	url(r'^find/', views.find),
	url(r'^register/', views.register),
	url(r'^logout/', views.user_logout),
]