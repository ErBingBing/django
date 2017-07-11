# conding=utf-8
from django.shortcuts import redirect


def user_long(func):
    def fun1(request, *args, **kwargs):
        if request.session.has_key('uid'):
            return func(request, *args, **kwargs)
        else:
            return redirect('/user/login/')
    return fun1
