# -*- coding:utf-8 -*-

from django.conf.urls import url
from TxgBlog.views import *

'''
    作用：路由配置
    作者：唐香港
    时间：2018/3/22
'''

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^article_detial/$', article_detial, name='article_detial'),
    url(r'^about/$', about, name='about'),
    url(r'^book/$', book, name='book'),
    url(r'^doing/$', doing, name='doing'),
    url(r'^ACM/$', ACM, name='ACM'),
    url(r'^coding/$', coding, name='coding'),
    url(r'^contact/$', contact, name='contact'),
]
