import urllib2

url = "http://www.baidu.com"
res = urllib2.urlopen(url)
savefile = open('../templates/save/baidu.html', 'w+')
savefile.write(res.read())
save.close()
