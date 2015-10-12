from django.conf.urls import patterns,  include, url
from django.contrib import admin
from follow_the_girl import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^baidu/', views.baidu),
	url(r'^test/', views.test),
]