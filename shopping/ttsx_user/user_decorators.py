# coding=utf-8
from django.shortcuts import redirect


def user_login(func):
    # 判断用户是否登录
    def func1(request, *args, **kwargs):
        if request.session.has_key('uid'):
            # 如果登录，则继续执行视图
            return func(request, *args, **kwargs)
        else:
            # 如果没有登录，则转到登录也
            return redirect('/user/login/')
    return func1
