#coding:utf-8
from django.shortcuts import render,render_to_response
import urllib2
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
#from datetime import datetimes
from django.contrib.auth.models import User
from follow_the_girl.models import tb_use_map_id,tb_follow_info
from django.shortcuts import redirect
from django.template import RequestContext
from follow_the_girl.forms import UserForm
from follow_the_girl.getdata import add_use_map_id,add_tb_follow_info
from random import randrange
from follow_the_girl.search import user_show
from follow_the_girl.spider import spider, analysis_info, spider_1, analysis_weibo, openfile
from follow_the_girl.getdata import add_User
# Create your views here.


def save(request):
    return render(request, 'save/test.html')

def weibo(request):
    username = User.objects.get(username=request.user.username)
    user_id = tb_use_map_id.objects.get(user_name=username)
    who = tb_follow_info.objects.get(user_id=user_id)
    str_html = spider_1(who.weibo_id, 0)
    str_weibo = analysis_weibo(str_html)
    str_weibo = '{% extends "base1.html" %}{% block body_block %}'+' <div class="pms">微博-<a href="/index/yuanchuang">原创</a>-<a href="/index/tupian">图片</a></div>'+str_weibo+'{% endblock body_block %}}'
    openfile('/home/itcast/webo/The_Girl/templates/index/weibo.html',str_weibo)
    return render(request, 'index/weibo.html')


def yuanchuang(request):
    username = User.objects.get(username=request.user.username)
    user_id = tb_use_map_id.objects.get(user_name=username)
    who = tb_follow_info.objects.get(user_id=user_id)
    str_html = spider_1(who.weibo_id, 1)
    str_weibo = analysis_weibo(str_html)
    str_weibo = '{% extends "base1.html" %}{% block body_block %}'+' <div class="pms"><a href="/index/weibo/">微博</a>-原创-<a href="/index/tupian">图片</a></div>'+str_weibo+'{% endblock body_block %}}'
    openfile('/home/itcast/webo/The_Girl/templates/index/yuanchuang.html',str_weibo)
    return render(request, 'index/yuanchuang.html')

def tupian(request):
    username = User.objects.get(username=request.user.username)
    user_id = tb_use_map_id.objects.get(user_name=username)
    who = tb_follow_info.objects.get(user_id=user_id)
    str_html = spider_1(who.weibo_id, 2)
    str_weibo = analysis_weibo(str_html)
    str_weibo = '{% extends "base1.html" %}{% block body_block %}'+' <div class="pms"><a href="/index/weibo/">微博</a>-<a href="/index/yuanchuang">原创</a>-图片</div>'+str_weibo+'{% endblock body_block %}}'
    openfile('/home/itcast/webo/The_Girl/templates/index/tupian.html',str_weibo)
    return render(request, 'index/tupian.html')

def index(request):
    if request.user.username != '':
        username = User.objects.get(username=request.user.username)
        user_id = tb_use_map_id.objects.get(user_name=username)
        who = tb_follow_info.objects.get(user_id=user_id)
        str_html = spider(who.weibo_id,'')
        follow_dict = analysis_info(str_html)
        follow_add = str(int(follow_dict['follow'])-int(who.follow))
        fans_add = str(int(follow_dict['fans'])-int(who.fans))
        tc_add = str(int(follow_dict['tc'])-int(who.tc))
        obj = tb_follow_info.objects.get(user_id=who.user_id)
        obj.follow = follow_dict['follow']
        obj.fans = follow_dict['fans']
        obj.tc = follow_dict['tc']
        obj.follow_add = follow_add
        obj.fans_add = fans_add
        obj.tc_add = tc_add
        obj.save()
        who = tb_follow_info.objects.get(user_id=user_id)
        who_dict = {}
        who_dict['who'] = who
        return render(request, 'index/index.html',who_dict)
    else:
        return render(request, 'index/login.html')


def usr_login(request):
    # If HTTP POST, pull out form data and process it.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index/search/')
            else:
                return render(request, 'index/login.html')
        else:
            return render(request, 'index/login.html')
    else:
        return render(request, 'index/login.html')

# def usr_login(request):
#     return render(request, 'index/search.html')

def search(request):
	return render(request, 'index/search.html')

def find(request):
    t_dict = {}
    if request.method == 'POST':
        data = request.POST['keyword']
        if data:
            allshow_dict = user_show(request,data)
            if allshow_dict and allshow_dict['id']:         
                str_html = spider(allshow_dict['id'],'')
                follow_dict = analysis_info(str_html)
                t_dict = dict(allshow_dict.items()+follow_dict.items())
                print t_dict
                return render(request, 'index/search.html',t_dict)
            else:
                return render(request, 'index/search.html')
        else:
            return render(request, 'index/search.html')
    return render(request, 'index/search.html')

#{{id}}:{{screen_name}}:{{location}}:{{ gender }}:{{ follow }}:{{ fans }}:{{ tc }}:{{ profile_image_url }}:{{url}}
def save_id(request):
    if_followed = False
    if request.method == 'POST':
        weibo_info = request.POST['weibo_info']
        print weibo_info
        w_id = weibo_info.split(':')[0]
        weibo_id = weibo_info.split(":")[0]
        weibo_sreen_name = weibo_info.split(":")[1]
        location = weibo_info.split(":")[2]
        gender = weibo_info.split(":")[3]
        follow = weibo_info.split(":")[4]
        fans = weibo_info.split(":")[5]
        tc = weibo_info.split(":")[6]
        profile_image_url = weibo_info.split(":")[7]
        profile_image_url = profile_image_url + ':' +weibo_info.split(":")[8]
        blog_address = ''
        if gender == 'f':
            gender = '女'
        else:
            gender = '男'
        username = User.objects.get(username=request.user)
        use_map = tb_use_map_id.objects.get(user_name=username)
        add_tb_follow_info(weibo_id,use_map.user_id,weibo_sreen_name,location,gender,profile_image_url,blog_address,follow,fans,tc)
        return render(request, 'index/index.html')
    else:
        return  render(request, 'index/search.html')
 

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #cd = form.cleaned_data
            user = form.save()
            user.set_password(user.password)
            user.save()
            rands = randrange(90000,100000)
            user_id = user.username+str(rands)
            add_use_map_id(user_id,user.username)
            return HttpResponseRedirect('/')
    else:
        form = UserForm(
            initial={'usename': 'I love !'}
        )
    return render_to_response('index/register.html', {'form': form})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/index/')