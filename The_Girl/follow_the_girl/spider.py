#coding:utf8
import urllib2
import re
import urllib
import cookielib
from bs4 import BeautifulSoup

def spider(id, key):
	cookie = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
	#url = 'http://weibo.cn/1230663070/info'
	url = 'http://weibo.cn/'
	#url = url+str(id)+'/'+str(key)
	url = url+str(id)
	urllogin = 'https://login.weibo.cn/login/'
	req_header = {
		'User-Agent' : 'splier',
	}
	req = urllib2.Request(urllogin, '', req_header)
	res = urllib2.urlopen(req)
	soup = BeautifulSoup(res.read(), 'lxml')
	password = soup.find("input", type = "password")["name"]
	vk = soup.find_all("input", type = "hidden")[3]["value"]
	action = soup.find("form",  method = "post")["action"]
	data = urllib.urlencode({
		'mobile':'123lixueyan@163.com',
		password:'abcd134556',
		'remember':'on',
		'backURL':url,
		'backTitle':'微博',
		'tryCount': '',
		'vk':vk,
		'submit':'登录',
	})
	newurl = urllogin+action
	req = urllib2.Request(newurl, data, req_header) 
	res = opener.open(req)
	return res.read()

def analysis_info(str_html):
	soup = BeautifulSoup(str_html, 'lxml')
	tc = soup.find("div", class_="tip2").span.string.split("[")[1].split("]")[0]
	follow = soup.find("div", class_="tip2").find_all('a')[0].string.split("[")[1].split("]")[0]
	fans = soup.find("div", class_="tip2").find_all('a')[1].string.split("[")[1].split("]")[0]
	follow_dict = {}
	follow_dict['tc'] = tc
	follow_dict['follow'] = follow
	follow_dict['fans'] = fans
	return follow_dict


def spider_1(id, key):
	cookie = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
	#url = 'http://weibo.cn/u/1828602435?filter=1'
	url = 'http://weibo.cn/'
	url = url+'u/'+str(id)+'?filter='+str(key)
	urllogin = 'https://login.weibo.cn/login/'
	req_header = {
		'User-Agent' : 'splier',
	}
	req = urllib2.Request(urllogin, '', req_header)
	res = urllib2.urlopen(req)
	soup = BeautifulSoup(res.read(), 'lxml')
	password = soup.find("input", type = "password")["name"]
	vk = soup.find_all("input", type = "hidden")[3]["value"]
	action = soup.find("form",  method = "post")["action"]
	data = urllib.urlencode({
		'mobile':'123lixueyan@163.com',
		password:'abcd134556',
		'remember':'on',
		'backURL':url,
		'backTitle':'微博',
		'tryCount': '',
		'vk':vk,
		'submit':'登录',
	})
	newurl = urllogin+action
	req = urllib2.Request(newurl, data, req_header) 
	res = opener.open(req)
	#print res.read()
	return res.read()

def openfile(path, str_html):
	f = open(path, 'w+')
	f.write(str_html)
	f.close()
	return True
#str_weibo = "{% extends "base.html" %}{% block body_block %}"+str_weibo+"{% endblock body_block %}}"
#f = open('/home/itcast/webo/The_Girl/templates/index/weibo.html', 'w+')
def analysis_weibo(str_html):
	soup = BeautifulSoup(str_html, 'lxml')
	str_weibo1 = soup.find_all('div', class_ = 'c')[0]
	str_weibo2= soup.find_all('div', class_ = 'c')[1]
	str_weibo3 = soup.find_all('div', class_ = 'c')[2]
	str_weibo4 = soup.find_all('div', class_ = 'c')[3]
	str_weibo1 = str(str_weibo1)
	str_weibo2 = str(str_weibo2)
	str_weibo3 = str(str_weibo3)
	str_weibo4 = str(str_weibo4)
	str_weibo = str_weibo1+str_weibo2+str_weibo3+str_weibo4
	return str_weibo

