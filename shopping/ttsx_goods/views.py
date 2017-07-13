# coding=utf-8
from django.shortcuts import render
from models import *
from django.http import HttpResponse

# Create your views here.


def index(request):
    goods_list = []
    typelist = TypeInfo.objects.all()
    goodlist = GoodsInfo.objects.all()
    # 四个最热商品
    # 四个点击量高的商品
    for t in typelist:
        nlist = t.goodsinfo_set.order_by('-id')[0:4]
        clist = t.goodsinfo_set.order_by('-gclick')[0:4]
        goods_list.append({'t': t, 'nlist': nlist, 'clist': clist})
    content = {'title': '首页', 'goods_list': goods_list, 'show_care': '1'}
    return render(request, 'ttsx_goods/index.html', content)


def list(request):
    return HttpResponse('ok')
