# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.


'''
    类作用：文章管理自定义
    作者：唐香港
    时间：2018/3/20
'''


class ArticleAdmin(admin.ModelAdmin):
    # 富文本编辑器的配置
    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )

# 将models的类注册进来

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(Article,ArticleAdmin)

