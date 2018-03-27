# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here

'''
    类作用：管理统计评论数量
    作者：唐香港
    时间：2018/3/20
'''


class ReviewManager(models.Manager):
    def review_count(self):
        return self.all().count()


'''
    类作用：用户数据库模型（采用继承的方法，需要在settings中配置相关属性）
    作者：唐香港
    时间：2018/3/20
'''


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d',default='avatar/default.png',max_length=200,blank = True,null = True,verbose_name='头像')
    qq = models.CharField(max_length=20,blank=True,null=True,verbose_name='qq号码')
    mobile = models.CharField(max_length=11,blank=True,null=True,unique=True,verbose_name='手机号码')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username


'''
    类作用：标签模型
    作者：唐香港
    时间：2018/3/20
'''


class Tag(models.Model):
    name = models.CharField(max_length=30,verbose_name='标签名称')

    class Meta:
        verbose_name='标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


'''
    类作用：文章模型
    作者：唐香港
    时间：2018/3/20
'''


class Article(models.Model):

    title = models.CharField(max_length=50,verbose_name='文章标题')
    desc = models.CharField(max_length=300,verbose_name='文章描述')
    content = models.TextField(verbose_name='文章内容')
    click_count = models.IntegerField(default=0,verbose_name='点击次数')
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    user = models.ForeignKey(User,verbose_name='用户')
    tag = models.ForeignKey(Tag, blank=True, null=True, verbose_name='标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
            return self.title


'''
    类作用：评论模型
    作者：唐香港
    时间：2018/3/20
'''


class Review(models.Model):
    content = models.TextField(verbose_name='评论内容',default='来呀，留言呀！')
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    user = models.CharField(max_length=50, verbose_name='用户',default='vision')
    email = models.CharField(max_length=50, verbose_name='邮箱',default='2411771853@qq.com')
    pid = models.ForeignKey('self',blank=True,null=True,verbose_name='父级评论')

    objects = ReviewManager()

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return str(self.id)