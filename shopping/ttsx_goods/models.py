# coding=utf-8
from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class TypeInfo(models.Model):
    # 类型名称
    ttitle = models.CharField(max_length=20)
    # 是否删除
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle.encode('utf-8')


class GoodsInfo(models.Model):
    # 商品名称
    gtitle = models.CharField(max_length=50)
    # 商品图片
    gpic = models.ImageField(upload_to='goods/')
    # 商品价格 999.99
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    # 商品点击量
    gclick = models.IntegerField(default=0)
    # 商品单位
    gunit = models.CharField(max_length=20)
    # 商品逻辑删除
    isDelete = models.BooleanField(default=False)
    # 商品子标题
    gsubtitle = models.CharField(max_length=200)
    # 商品库存
    gkucun = models.IntegerField(default=200)
    # 商品内容
    gcontent = HTMLField()
    # 商品类型
    gtype = models.ForeignKey('TypeInfo')
