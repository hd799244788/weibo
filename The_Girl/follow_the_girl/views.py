from django.shortcuts import render
import urllib2
# Create your views here.

'''sys.setdefaultencoding('utf-8')'''
# -*- coding: utf-8 -*-
def index (request):
	return render(request, 'index/index.html')

def baidu(request):
	url = 'http://weibo.com/hangeng?from=1087030002_892_1003_0'

	res = urllib2.urlopen(url)
	savefile = open('/home/itcast/webo/The_Girl/templates/save/baidu.html', 'w+')
	savefile.write(res.read().decode("GBK").encode("utf-8"))
	#savefile.write(res.read())
	savefile.close()
	return render(request, 'save/baidu.html')


def test(request):
	return render(request, 'save/test.html')
