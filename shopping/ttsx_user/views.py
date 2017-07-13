# coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from hashlib import sha1
from models import *
import datetime
from user_decorators import *


# Create your views here.
# 注册
def register(request):
    content = {'title': '注册', 'top': '0'}
    return render(request, 'ttsx_user/register.html', content)


# 注册用户放入数据库
def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('user_pwd')
    uemil = post.get('user_email')
    # 密码加密
    s1_pwd = s1(upwd)
    # 创建对象
    userinfo = userInfo()
    userinfo.uname = uname
    userinfo.upwd = s1_pwd
    userinfo.umail = uemil
    userinfo.save()
    return redirect('/user/login/')


# 判断用户名是否存在
def isName(request):
    uname = request.GET.get('uname')
    result = userInfo.objects.filter(uname=uname).count()
    return JsonResponse({'result': result})


# 登录
def login(request):
    uname = request.COOKIES.get('usercook', '')
    content = {'title': '登录', 'uname': uname, 'top': '0'}
    return render(request, 'ttsx_user/login.html', content)


# 登录处理
def login_handle(request):
    uname = request.POST.get('username')
    upwd = request.POST.get('userpwd')
    ucookie = request.POST.get('ucookie')
    s1_pwd = s1(upwd)

    unamelen = userInfo.objects.filter(uname=uname)
    if (len(unamelen) == 0):
        # 用户名错误
        countent = {'uerro': 1, 'uname': uname,
                    'upwd': upwd, 'title': '登录', 'top': '0'}
        return render(request, 'ttsx_user/login.html/', countent)
    else:
        upwdlen = userInfo.objects.filter(upwd=s1_pwd)
        request.session['uid'] = unamelen[0].id
        request.session['uanme'] = uname
        if(len(upwdlen) == 0):
            # 密码错误
            countent = {'perro': 1, 'uname': uname,
                        'upwd': upwd, 'title': '登录', 'top': '0'}
            return render(request, 'ttsx_user/login.html/', countent)
        else:
            urlpath = request.session.get('url_path', '/')
            response = redirect(urlpath)
            if ucookie == '1':
                response.set_cookie(
                    'usercook', uname, expires=datetime.datetime.now() + datetime.timedelta(days=7))
            else:
                response.set_cookie('usercook', '', max_age=-1)
                # return render(request, 'ttsx_user/index.html/')
            return response


# 首页
# def index(request):
#     userlist = userInfo.objects.all()
#     context = {'userInfo': userlist}
#     return render(request, 'ttsx_user/index.html', context)


# 退出
def loginout(request):
    request.session.flush()
    return redirect('/user/login/')


# 用户页面个人信息
@user_long
def info(request):
    user = userInfo.objects.get(pk=request.session['uid'])
    content = {'title': '用户中心', 'username': user.uname,
               'email': user.umail, 'display': '1'}
    return render(request, 'ttsx_user/info.html', content)


# 用户页面订单
@user_long
def order(request):
    content = {'title': '用户中心'}
    return render(request, 'ttsx_user/order.html', content)


# 用户页面收货地址
@user_long
def site(request):
    user = userInfo.objects.get(pk=request.session['uid'])
    if request.method == 'POST':
        user.ushou = request.POST.get('ushou')
        user.uaddress = request.POST.get('uaddress')
        user.ucode = request.POST.get('ucode')
        user.uphone = request.POST.get('uphone')
        user.save()
    content = {'title': '用户中心', 'user': user}
    return render(request, 'ttsx_user/site.html', content)

# sha1加密


def s1(upwd):
    s1 = sha1()
    s1.update(upwd)
    s1_pwd = s1.hexdigest()
    return s1_pwd


# 测试函数
def test(request):
    return render(request, 'base.html', {'title': 'haha'})