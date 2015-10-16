#coding:utf-8
from django.shortcuts import render
import urllib2
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.template import RequestContext
from follow_the_girl.forms import UserForm
from follow_the_girl.getdata import add_use_map_id
from random import randrange
# Create your views here.



def index(request):
    return render(request, 'index/index.html')

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

def search(request):
	return render(request, 'index/search.html')

def find(request):
	if request.method == 'POST':
		return render(request, 'save/baidu.html')
	return render(request, 'save/test.html')

def register(request):
    context_dict = {}
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            rands = randrange(90000,100000)
            user_id = user.username+str(rands)
            add_use_map_id(user_id,user.username)
            return render(request, 'index/login.html')
        else:
            print user_form.errors
    else:
	user_form = UserForm()
    context_dict["user_form"] = user_form
    return render(request, 'index/register.html', context_dict)