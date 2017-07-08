#coding=utf-8
from django.db import models

# Create your models here.


class userInfo(models.Model):
    # 用户名
    uname = models.CharField(max_length=30)
    # 密码
    upwd = models.CharField(max_length=40)
    # 邮箱
    umail = models.CharField(max_length=40)
    # 收货
    ushou = models.CharField(max_length=40, default='')
    # 地址
    uaddress = models.CharField(max_length=40, default='')
    # 邮编
    ucode = models.CharField(max_length=6, default='')
    # 手机号
    uphone = models.CharField(max_length=6, default='')
