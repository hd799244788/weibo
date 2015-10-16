#coding:utf8
import re
import urllib2
from follow_the_girl.models import tb_follow_info, tb_counter ,tb_use_map_id
from bs4 import BeautifulSoup

#getdata from org  and save into db

def add_use_map_id(use_id,use_name):
	tb_use_map_id.objects.get_or_create(use_id=use_id, use_name=use_name)
	return True

def add_counter(use_id,follow, fans, tc):
	counter = tb_counter.objects.get_or_create(use_id=use_id,follow=follow, fans=fans, tc=tc)[0]
	return counter

def add_follow_info(use_id, usename, password, level, place, constellation, brief_introduction, mail, blog_address, relationship):
	follow_info = tb_follower_info.objects.get_or_create(use_id=use_id,usename=usename,password=password, level=level, place=place, constellation=constellation, brief_introduction=brief_introduction, mail=mail, blog_address=blog_address, relationship=relationship)[0]
	return follow_info

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

	follow_info = add_follow_info(
		use_id,
		'huangdi',
		'huangdi',
		99,
                        '北京　昌平区　中腾建华',
                        '天平座',
                        '更改MySQL数据库表中某个字段的字符集',
                        '799244788@qq.com',
                        '799244788@qq.com',
                        'single dog',               
	)
	return True