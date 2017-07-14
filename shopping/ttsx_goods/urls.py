# coding=utf-8
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^good_list(\d+)_(\d+)/$',views.good_list),
    url(r'^(\d+)/$',views.detail),
]
