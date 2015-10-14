from django.db import models

# Create your models here.

class tb_counter(models.Model):
	use_id = models.IntegerField(unique=True)
	follow = models.IntegerField()
	fans = models.IntegerField()
	tc = models.IntegerField()
	def __unicode__(self):
		return self.follow

class tb_follower_info(models.Model):
	#info
	use_id = models.IntegerField(unique=True)
	usename = models.CharField(max_length=128)
	password = models.CharField(max_length=128)
	level = models.IntegerField()
	place = models.CharField(max_length=128)
	constellation = models.CharField(max_length=128)
	brief_introduction = models.CharField(max_length=128)
	mail = models.EmailField()
	blog_address = models.URLField()
	relationship = models.CharField(max_length=128)
	
	def __unicode__(self):
		return "tb_follower_info"




class tb_favor(models.Model):
	favor_picture = models.URLField()
	favor_music = models.URLField()
	favor_place = models.URLField()
	favor_movie = models.URLField()
	favor_weibo = models.URLField()
	def __unicode__(self):
		return "tb_favor"

class tb_weibo(models.Model):
	weibo_info = models.URLField()
	repeat_list = models.URLField()
	class Meta:
        		verbose_name = "MODELNAME"
        		verbose_name_plural = "MODELNAMEs"
	def __unicode__(self):
		return "tb_weibo"