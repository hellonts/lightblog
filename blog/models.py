# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from datetime import datetime as dt
from django.utils import timezone


class Tag(models.Model):
    name                = models.CharField(max_length=25,verbose_name=u'标签')
    publish_time        = models.DateTimeField(auto_now_add=True,verbose_name=u'加入时间')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-publish_time']
        verbose_name = '标签'


class Comment(models.Model):
    tid                 = models.ForeignKey('Topic',to_field='id',db_column='tid',related_name='tid',verbose_name=u'文章ID')
    comment             = models.TextField(verbose_name=u'内容')
    hide                = models.BooleanField(default=False,verbose_name=u'是否转入草稿箱')
    publish_time        = models.DateTimeField(auto_now_add=True,verbose_name=u'加入时间')

    def __unicode__(self):
        return self.caption

    class Meta:
        ordering = ['-publish_time']
        verbose_name = '回复'


class SecondClass(models.Model):
    name                = models.CharField(max_length=50,verbose_name=u'名称')
    publish_time        = models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')
    count				= models.CharField(max_length=10,verbose_name=u'数量',blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '二级分类'


class OneClass(models.Model):
    name                = models.CharField(max_length=50,verbose_name=u'名称')
    secondclass         = models.ManyToManyField(SecondClass,verbose_name=u'二级分类')
    publish_time        = models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'一级分类'


class Topic (models.Model):
    caption             = models.CharField(max_length=50,verbose_name=u'标题')
    content             = models.TextField(verbose_name=u'内容')
    topicimg			= models.FileField(upload_to='topic_img',verbose_name=u'封面图',blank=True,null=True)
    author              = models.ForeignKey(User,to_field='username',db_column='author',related_name='author',
                                            verbose_name=u'作者')
    tags                = models.ManyToManyField(Tag,blank=True,verbose_name=u'标签')
    views               = models.IntegerField(default=0, verbose_name=u'浏览数')
    comnum              = models.IntegerField(default=0,verbose_name=u'评论数')
    top                 = models.BooleanField(default=False,verbose_name=u'是否置顶')
    sorttop             = models.BooleanField(default=False,verbose_name=u'是否分类置顶')
    hide                = models.BooleanField(default=False,verbose_name=u'是否转入草稿')
    allow_remark        = models.BooleanField(default=True,verbose_name=u'是否评论')
    digest              = models.BooleanField(default=False,verbose_name=u'是否加精')
    password            = models.CharField(max_length=50,blank=True,verbose_name=u'文章加密密码')
    topic_subclass      = models.ForeignKey(SecondClass,verbose_name=u'二级类别')
    publish_time        = models.DateTimeField(auto_now_add=True,verbose_name=u'加入时间')
    update_time         = models.DateTimeField(auto_now_add=True,verbose_name=u'更新时间')

    def __unicode__(self):
        return self.caption

    class Meta:
        ordering = ['-publish_time']
        verbose_name = '文章'


class Options(models.Model):
    option_name = models.CharField(max_length=50,verbose_name=u'名称')
    option_key = models.CharField(max_length=50,verbose_name=u'key')
    option_value = models.CharField(max_length=80,verbose_name=u'value')
    publish_time = models.DateTimeField(auto_now_add=True,verbose_name=u'加入时间')

    def __unicode__(self):
        return self.option_name

    class Meta:
        ordering = ['-publish_time']
        verbose_name = '系统设置'


class Link(models.Model):
    sitename = models.CharField(max_length=20)#链接名称
    siteurl  = models.URLField(max_length=100)#链接地址
    description = models.CharField(max_length=30)#链接说明
    hide = models.BooleanField(default=False)#是否转入草稿箱
    sort = models.IntegerField(default=0)#排序
    publish_time = models.DateTimeField(auto_now_add=True)#时间

    def __unicode__(self):
        return self.sitename

    class Meta:
        ordering = ['sort']
        verbose_name = '友链'


class ProfileBase(type):
    def __new__(cls, name, bases, attrs):
        module = attrs.pop('__module__')
        parents = [b for b in bases if isinstance(b, ProfileBase)]
        if parents:
            fields = []
            for obj_name, obj in attrs.items():
                if isinstance(obj, models.Field): fields.append(obj_name)
                User.add_to_class(obj_name, obj)
            UserAdmin.fieldsets = list(UserAdmin.fieldsets)
            UserAdmin.fieldsets.append((name, {'fields': fields}))
        return super(ProfileBase, cls).__new__(cls, name, bases, attrs)


class Profile(object):
    __metaclass__ = ProfileBase


class MyProfile(Profile):
    nickname            = models.CharField(max_length = 30, blank = True,verbose_name=u'昵称')
    giturl              = models.URLField(max_length=100,blank=True,verbose_name=u'git个人主页')
    city                = models.CharField(max_length = 30, blank = True,verbose_name=u'城市')
    gender              = models.CharField(max_length = 10, blank = True,verbose_name=u'性别')
    job                 = models.CharField(max_length=50, blank= True,verbose_name=u'职业')
    synopsis            = models.TextField(max_length=255, blank= True,verbose_name=u'简介')
    avatar_img          = models.FileField(upload_to='topic_img',blank = True,verbose_name=u'头像')

    def __unicode__(self):
        return self.nickname

    class Meta:
        verbose_name = '扩展用户'
