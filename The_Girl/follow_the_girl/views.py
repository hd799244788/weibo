#coding:utf-8
from django.shortcuts import render
import urllib2
from follow_the_girl.models import tb_counter, tb_follower_info
# Create your views here.

'''sys.setdefaultencoding('utf-8')'''


import re

from bs4 import BeautifulSoup

from follow_the_girl.getdata import getdata


# -*- coding: utf-8 -*-
def index (request):
	getdata(request)

	context_dict = {}
	counters = tb_counter.objects.order_by('follow')
	context_dict['counters'] = counters
	infos = tb_follower_info.objects.order_by('level')
	context_dict['infos'] = infos

	return render(request, 'index/index.html', context_dict)


import cookielib





def baidu(request):
	url = 'http://weibo.cn/tangyan'
	req_header = {
		'User-Agent' : 'splier'
	}
	req = urllib2.Request(url, '', req_header)
	res = urllib2.urlopen(req)

	savefile = open('/home/itcast/webo/The_Girl/templates/save/baidu.html', 'w+')
	savefile.write(res.read())
	#savefile.write(res.read().decode("GBK").encode("utf-8"))
	savefile.close()
	return render(request, 'save/baidu.html')


def test(request):
	return render(request, 'save/test.html')

