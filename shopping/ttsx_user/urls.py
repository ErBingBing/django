# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    # 注册
    url(r'^register/', views.register),
    url(r'^register_handle/', views.register_handle),
    # 判断用户名是否存在
    url(r'^isName/', views.isName),
    # 登录
    url(r'^login/', views.login),
    # 登录处理
    url(r'^login_handle/', views.login_handle),
    # 用户
    # url(r'^$', views.index),
    # 用户退出
    url(r'^loginout/', views.loginout),
    # 用户信息
    url(r'^info/', views.info),
    # 用户订单
    url(r'^order/', views.order),
    # 用户收货地址
    url(r'^site/', views.site),











    # test url
    url(r'^test/$', views.test),
]
