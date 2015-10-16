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

class UserProfile(models.Model):
	# A required line - links a UserProfile to User.
	user = models.OneToOneField(User)
	
	# The additional attributes we wish to include.
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	
	def __unicode__(self):
		return self.user.username
