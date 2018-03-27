# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,render_to_response
from django.template import loader, Context, RequestContext
from django.conf import settings
from django.db.models import Count
from django.views.generic.edit import FormView
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django import forms
from django.shortcuts import render
from models import *
import markdown
# Create your views here.

'''
    类作用：生成表单
    作者：唐香港
    时间：2018/3/22
'''


class ContactForm(forms.Form):
    message = forms.CharField(required=True,widget=forms.Textarea(), initial="既然来了就说点什么吧.....", label='说点什么好呢！')
    subject = forms.CharField(required=True,max_length=100,label='昵称',widget=forms.TextInput(attrs={'class': 'f2'}))
    sender = forms.EmailField(required=True,initial='your_email@163.com',label='邮箱',widget=forms.TextInput(attrs={'class': 'f3'}))


'''
    函数作用：博客分页
    作者：唐香港
    时间：2018/3/21
'''


def getPage(request,article_list,page1):
    paginator = Paginator(article_list, page1)
    # 做异常处理，传的数据可能会出现异常
    try:
        # 获取当前页分页的数据的页码
        page = int(request.GET.get('page', 1))
        # 把当前页传入分页的列表中
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        # 出异常后默认显示第一页
        article_list = paginator.page(1)
    return article_list


'''
    函数作用：显示博客主页
    作者：唐香港
    时间：2018/3/20
'''


def index(request):
    try:
        if not request.user.is_authenticated():
            article_list = Article.objects.exclude(tag__name='碎言碎语')
        article_list = Article.objects.exclude(tag__name='碎言碎语')
        article_list_all_one = article_list.order_by('-date_publish')[:min(len(article_list), 8)]
        article_list_all_two = article_list.order_by('click_count')[:min(len(article_list), 5)]
        article_list = getPage(request, article_list, 6)
    except Exception as e:
        pass
    return render(request,'index.html',locals())


'''
    函数作用：显示文章详细内容
    作者：唐香港
    时间：2018/3/21
'''


def article_detial(request):
    try:
        article_list_all = Article.objects.exclude(tag__name='碎言碎语')
        article_list_all_one = article_list_all.order_by('-date_publish')[:min(len(article_list_all), 8)]
        article_list_all_two = article_list_all.order_by('click_count')[:min(len(article_list_all), 5)]
        id = request.GET.get('id')
        article_list = Article.objects.get(pk=id)
        article_list.click_count = article_list.click_count + 1
        article_list.save()
        article_list = markdown.markdown(article_list)
    except Exception as e:
        pass
    return render(request, 'article_detial.html', locals())


'''
    函数作用：关于我页面
    作者：唐香港
    时间：2018/3/21
'''


def about(request):
    return render(request, 'about.html', locals())


'''
    函数作用：百草屋类型的文章页面
    作者：唐香港
    时间：2018/3/21
'''

def book(request):
    try:
        article_list_all = Article.objects.exclude(tag__name='碎言碎语')
        article_list_all_one = article_list_all.order_by('-date_publish')[:min(len(article_list_all), 8)]
        article_list_all_two = article_list_all.order_by('click_count')[:min(len(article_list_all), 5)]
        article_list = []
        if not request.user.is_authenticated():
            article_list = Article.objects.filter(tag__name="百草屋")
        article_list = Article.objects.filter(tag__name="百草屋")

        article_list = getPage(request, article_list, 6)
    except Exception as e:
        pass
    return render(request, 'book.html', locals())


'''
    函数作用：碎言碎语类型的文章页面
    作者：唐香港
    时间：2018/3/21
'''


def doing(request):
    try:
        article_list = []
        if not request.user.is_authenticated():
            article_list = Article.objects.filter(tag__name="碎言碎语")
        article_list = Article.objects.filter(tag__name="碎言碎语")
        article_list = getPage(request, article_list, 6)
    except Exception as e:
        pass
    return render(request, 'doing.html', locals())


'''
    函数作用：算法模板文章页面
    作者：唐香港
    时间：2018/3/21
'''


def ACM(request):
    try:
        article_list_all = Article.objects.exclude(tag__name='碎言碎语')
        article_list_all_one = article_list_all.order_by('-date_publish')[:min(len(article_list_all), 8)]
        article_list_all_two = article_list_all.order_by('click_count')[:min(len(article_list_all), 5)]
        article_list = []
        if not request.user.is_authenticated():
            article_list = Article.objects.filter(tag__name="算法模板")
        article_list = Article.objects.filter(tag__name="算法模板")

        article_list = getPage(request, article_list, 6)
    except Exception as e:
        pass
    return render(request,'ACM.html',locals())



'''
    函数作用：代码控文章页面
    作者：唐香港
    时间：2018/3/21
'''


def coding(request):
    try:
        article_list_all = Article.objects.exclude(tag__name='碎言碎语')
        article_list_all_one = article_list_all.order_by('-date_publish')[:min(len(article_list_all), 8)]
        article_list_all_two = article_list_all.order_by('click_count')[:min(len(article_list_all), 5)]
        article_list = []
        if not request.user.is_authenticated():
            article_list = Article.objects.filter(tag__name="代码控")
        article_list = Article.objects.filter(tag__name="代码控")

        article_list = getPage(request, article_list, 6)
    except Exception as e:
        pass
    return render(request,'coding.html',locals())


'''
    函数作用：留言板模块
    作者：唐香港
    时间：2018/3/22
'''


def contact(request):
    review_list=Review.objects.all()
    review_list = getPage(request, review_list, 10)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            mess_len = len(message)
            if mess_len < 4:
                raise forms.ValidationError("not enough word")
            subject = form.cleaned_data['subject']
            Review.objects.create(content=message, user=subject, email=sender)
            return HttpResponse('OK')
        else:
            return HttpResponse('NULL')
    else:
        form = ContactForm()
    return render(request, 'contact.html', locals())


