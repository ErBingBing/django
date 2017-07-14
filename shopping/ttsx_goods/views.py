# coding=utf-8
from django.shortcuts import render
from models import *
from django.http import HttpResponse
from django.core.paginator import Paginator
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


def good_list(request, tid, pindex):
    try:

        t1 = TypeInfo.objects.get(pk=int(tid))
        t2 = t1.goodsinfo_set.order_by('-id')
        new_list = t2[0:2]
        # 查询：当前分类的所有商品，按每页15个来显示
        paginator = Paginator(t2, 15)

        if int(pindex) < 1:
            pindex = 1
        elif int(pindex) > paginator.num_pages:
            pindex = paginator.num_pages
        page = paginator.page(pindex)

        conent = {'title': '商品列表', 'show_care': '1',
                  't1': t1, 'new_list': new_list, 'page': page}
        return render(request, 'ttsx_goods/list.html', conent)
    except:
        return render(request, '404.html')


def detail(request, id):
    try:
        good = GoodsInfo.objects.get(pk=int(id))
        good.gclick+=1
        good.save()
        new_list = good.gtype.goodsinfo_set.order_by('-id')[0:2]
        content = {'title': '商品详细', 'show_care': '1',
                   'good': good, 'new_list': new_list}
        return render(request, 'ttsx_goods/detail.html', content)
    except:
        return render(request, '404.html')
