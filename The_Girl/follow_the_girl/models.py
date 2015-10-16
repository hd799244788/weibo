from django.db import models
# Create your models here.

from django.contrib.auth.models import User

class tb_use_map_id(models.Model):
	use_id = models.CharField(max_length=128, unique=True)
	use_name = models.CharField(max_length=128)
	def __unicode__(self):
		return self.use_id

class tb_counter(models.Model):
	use_id = models.CharField(max_length=128, unique=True)
	follow = models.CharField(max_length=128, unique=True)
	fans = models.CharField(max_length=128, unique=True)
	tc = models.CharField(max_length=128, unique=True)
	
	def __unicode__(self):
		return self.use_id

class tb_follow_info(models.Model):
	use_id = models.CharField(max_length=128)
	place = models.CharField(max_length=128)
	constellation = models.CharField(max_length=128)
	brief_introduction = models.CharField(max_length=128)
	mail = models.CharField(max_length=128)
	blog_address = models.CharField(max_length=128)
	relationship = models.CharField(max_length=128)
	level = models.CharField(max_length=128)
	
	def __unicode__(self):
		return self.level

class tb_findout(models.Model):
	use_id = models.CharField(max_length=128)
	picture = models.CharField(max_length=128)
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