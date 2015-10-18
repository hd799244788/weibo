from django.db import models
# Create your models here.

from django.contrib.auth.models import User

class tb_use_map_id(models.Model):
	user_id = models.CharField(max_length=128, unique=True)
	user_name = models.CharField(max_length=128,unique=True)
	def __unicode__(self):
		return self.user_id

class tb_counter(models.Model):
	user_id = models.CharField(max_length=128, unique=True)
	follow = models.CharField(max_length=128)
	fans = models.CharField(max_length=128)
	tc = models.CharField(max_length=128)
	def __unicode__(self):
		return self.user_id

class tb_follow_info(models.Model):
	weibo_id = models.CharField(max_length=128)
	user_id = models.CharField(max_length=128,unique=True)
	screen_name = models.CharField(max_length=128)
	place = models.CharField(max_length=128)
	gender = models.CharField(max_length=128)
	profile_image_url = models.CharField(max_length=128)
	blog_address = models.CharField(max_length=128)
	follow = models.CharField(max_length=128)
	fans = models.CharField(max_length=128)
	tc = models.CharField(max_length=128)
	follow_add = models.CharField(max_length=128)
	fans_add = models.CharField(max_length=128)
	tc_add = models.CharField(max_length=128)
	def __unicode__(self):
		return self.user_id

class tb_findout(models.Model):
	user_id = models.CharField(max_length=128)
	weibo_id = models.CharField(max_length=128)
	profile_image_url = models.CharField(max_length=128)
	screen_name = models.CharField(max_length=128)
	loction = models.CharField(max_length=128)
	description = models.CharField(max_length=128)
	followers_count = models.CharField(max_length=128)
	friends_count = models.CharField(max_length=128)
	statuses_count = models.CharField(max_length=128)
	def __unicode__(self):
		return self.picture

class tb_struct(models.Model):
	w_id = models.CharField(max_length=128)
	screen_name = models.CharField(max_length=128)
	location = models.CharField(max_length=128)
	profile_image_url = models.CharField(max_length=128)
	gender = models.CharField(max_length=128)
	followers_count = models.CharField(max_length=128)
	friends_count = models.CharField(max_length=128)
	statuses_count = models.CharField(max_length=128)
	def __unicode__(self):
		return self.w_id