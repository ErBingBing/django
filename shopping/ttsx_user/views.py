# coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
from hashlib import sha1
from models import *


# Create your views here.
# 注册
def register(request):
    content = {'title': '注册'}
    return render(request, 'ttsx_user/register.html', content)


# 注册用户放入数据库
def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('user_pwd')
    uemil = post.get('user_email')
    # 密码加密
    s1 = sha1()
    s1.update(upwd)
    s1_pwd = s1.hexdigest()
    # 创建对象
    userinfo = userInfo()
    userinfo.uname = uname
    userinfo.upwd = s1_pwd
    userinfo.umail = uemil
    # userinfo.save()
    # return HttpResponse('ok')
    return redirect('/user/login/')

def login(request):
    content = {'title':'登录'}
    return render(request, 'ttsx_user/login.html', content)

def index(request):
    userlist = userInfo.objects.all()
    context = {'userInfo': userlist}
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # return HttpResponse(BASE_DIR)
    return render(request, 'ttsx_user/index.html', context)


# test views
def test(request):
    return render(request, 'base.html', {'title': 'haha'})
    # return HttpResponse('ok')
