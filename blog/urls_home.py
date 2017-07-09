#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *


urlpatterns = patterns(('blog.light_home'),

    # name属性是给这个url起个别名，可以在模版中引用而不用担心urls文件中url的修改 引用方式为{% url bloglist %}
     url(r'^$', 'blog_list', name='bloglist'),
     url(r'^(?P<second>\w+)/(?P<id>\d+)/(?P<caption>.*).html$', 'blog_show', name='blogshow'),
     url(r'^(?P<name>\w+)$', 'secondtopic_list', name='secondtopiclist'),


)
