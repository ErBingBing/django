# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    # 注册
    url(r'^register/', views.register),
    url(r'^register_handle/', views.register_handle),
    # 登录
    url(r'^login/', views.login),
    # 用户
    url(r'^$', views.index),









    # test url
    url(r'^test/$', views.test),
]
