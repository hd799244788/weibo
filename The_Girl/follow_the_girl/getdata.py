#coding:utf8
import re
import urllib2
from follow_the_girl.models import tb_follow_info, tb_counter ,tb_use_map_id
from bs4 import BeautifulSoup

#getdata from org  and save into db

def add_tb_follow_info(weibo_id,user_id='1234567',screen_name='',place='',gender='' ,profile_image_url = '',blog_address='',follow='',fans='',tc='',follow_add='0',fans_add='0',tc_add='0'):
	tb_follow_info.objects.get_or_create(weibo_id=weibo_id,user_id=user_id,screen_name=screen_name,place=place ,gender=gender,profile_image_url=profile_image_url,blog_address=blog_address,follow=follow,fans=fans,tc=tc,follow_add=follow_add,fans_add=fans_add,tc_add=tc_add)
	return True

def add_use_map_id(use_id,use_name):
	tb_use_map_id.objects.get_or_create(user_id=use_id, user_name=use_name)
	return True

def add_counter(use_id,follow, fans, tc):
	counter = tb_counter.objects.get_or_create(use_id=use_id,follow=follow, fans=fans, tc=tc)[0]
	return counter


def getdata(request):
	url = 'http://weibo.cn/yogalin'
	req_header = {
		'User-Agent' : 'splier'
	}
	req = urllib2.Request(url, '', req_header)
	res = urllib2.urlopen(req)

	soup = BeautifulSoup(res.read(), "lxml")

	tc = soup.find("div", class_="tip2").span.string.split("[")[1].split("]")[0]
	follow = soup.find("div", class_="tip2").find_all('a')[0].string.split("[")[1].split("]")[0]
	fans = soup.find("div", class_="tip2").find_all('a')[1].string.split("[")[1].split("]")[0]
	use_id = 100002
	for counter in tb_counter.objects.order_by('use_id'):
		if use_id == counter.use_id:
			return True

	add_counter(use_id, int(follow), int(fans), int(tc))
	return True