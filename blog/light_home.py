# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render, get_object_or_404
from models import *
from forms import *
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.core.exceptions import ObjectDoesNotExist
import json, os, datetime, time
import logging


def blog_list(request):
    title = u'博客列表'

    links = Link.objects.all()
    tags = Tag.objects.all()
    bkeywords = Options.objects.filter(option_key='keywords').last()
    bdescription = Options.objects.filter(option_key='description').last()
    bcop = Options.objects.filter(option_key='cop').last()
    breserved = Options.objects.filter(option_key='reserved').last()
    bname = Options.objects.filter(option_key='bname').last()
    btitle = Options.objects.filter(option_key='btitle').last()
    bgit = Options.objects.filter(option_key='github').last()
    digest = Topic.objects.filter(digest=True).order_by('publish_time').last()
    hottopic = Topic.objects.order_by('-views')[0:5]
    oneclass = OneClass.objects.all()
    secondclass = SecondClass.objects.all()     
    for i in secondclass:
        i.count = Topic.objects.filter(topic_subclass=i).count()
        i.save()
    user = User.objects.filter(is_superuser=True)[0]
    blogs = Topic.objects.filter(digest=False)
    paginator = Paginator(blogs, 8)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except (EmptyPage,InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('home/blog_list.html', locals(),context_instance=RequestContext(request))


def blog_show(request, second,id,caption, **kwargs):
    title = u'博客详情'

    pageurl = 'http://www.pythonkf.com%s'% request.get_full_path()
    links = Link.objects.all()
    bcop = Options.objects.filter(option_key='cop').last()
    breserved = Options.objects.filter(option_key='reserved').last()
    bname = Options.objects.filter(option_key='bname').last()
    btitle = Options.objects.filter(option_key='btitle').last()
    bgit = Options.objects.filter(option_key='github').last()
    digest = Topic.objects.filter(digest=True).order_by('publish_time').last()
    hottopic = Topic.objects.order_by('-views')[0:5]
    oneclass = OneClass.objects.all()
    tags = Tag.objects.all()
    user = User.objects.get(is_superuser=True)
    try:
        mess = Topic.objects.get(id=id)
        if mess:
            mess.views = int(mess.views) + 1
            mess.save()
    except Topic.DoesNotExist:
        raise Http404
    return render_to_response('home/blog_show.html', locals(),context_instance=RequestContext(request))


def secondtopic_list(request,name):
    title = u'二级分类博客列表'

    links = Link.objects.all()
    bcop = Options.objects.filter(option_key='cop').last()
    breserved = Options.objects.filter(option_key='reserved').last()
    bname = Options.objects.filter(option_key='bname').last()
    btitle = Options.objects.filter(option_key='btitle').last()
    bgit = Options.objects.filter(option_key='github').last()
    digest = Topic.objects.filter(digest=True).order_by('publish_time').last()
    hottopic = Topic.objects.order_by('-views')[0:5]
    oneclass = OneClass.objects.all()
    
    tags = Tag.objects.all()
    user = User.objects.get(is_superuser=True)
    secondclass = SecondClass.objects.filter(name=name)
    blogs = Topic.objects.filter(topic_subclass=secondclass)
    paginator = Paginator(blogs, 8)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except (EmptyPage,InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('home/secondtopic_list.html', locals(),context_instance=RequestContext(request))



