#coding:utf-8
import urllib2
import sys
import re
import base64
import json
from urlparse import urlparse
import simplejson
import time
#

def user_show(Request,name):
	usershow = 'https://api.weibo.com/2/users/show.json?screen_name=%(screen_name)s&source=%(source_key)d&'
	#how much day's data we will to search ,default is one week
	search_para={
			'screen_name':name.encode('utf-8'),
			'source_key':820439504,
		}
	usershow=usershow%search_para
	print usershow
	username = '123lixueyan@163.com'
	password = 'abcd134556'
	base64string = base64.encodestring('%s:%s' % (username, password))[:-1] #注意哦，这里最后会自动添加一个\n
	authheader =  "Basic %s" % base64string

	req=urllib2.Request(usershow)
	try:
		req.add_header("Authorization", authheader)
		print req
		handle = urllib2.urlopen(req).read()
	except Exception, e:
		return 0	
	print handle.decode("utf-8").encode("utf-8")
	allshow_dict =simplejson.loads(handle)
	return allshow_dict