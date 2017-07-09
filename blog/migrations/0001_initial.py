# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(verbose_name='\u5185\u5bb9')),
                ('hide', models.BooleanField(default=False, verbose_name='\u662f\u5426\u8f6c\u5165\u8349\u7a3f\u7bb1')),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name='\u52a0\u5165\u65f6\u95f4')),
                ('poster', models.ForeignKey(related_name='poster', db_column=b'poster', verbose_name='\u8bc4\u8bba\u4eba', to_field=b'username', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish_time'],
                'verbose_name': '\u56de\u590d',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sitename', models.CharField(max_length=20)),
                ('siteurl', models.URLField(max_length=100)),
                ('description', models.CharField(max_length=30)),
                ('hide', models.BooleanField(default=False)),
                ('sort', models.IntegerField(default=0)),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['sort'],
                'verbose_name': '\u53cb\u94fe',
            },
        ),
        migrations.CreateModel(
            name='OneClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u4e00\u7ea7\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('option_name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('option_key', models.CharField(max_length=50, verbose_name='key')),
                ('option_value', models.CharField(max_length=80, verbose_name='value')),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name='\u52a0\u5165\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-publish_time'],
                'verbose_name': '\u7cfb\u7edf\u8bbe\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='SecondClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('oneclass', models.ForeignKey(verbose_name='\u4e00\u7ea7\u7c7b\u522b', to='blog.OneClass')),
            ],
            options={
                'verbose_name': '\u4e8c\u7ea7\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name='\u6807\u7b7e')),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name='\u52a0\u5165\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-publish_time'],
                'verbose_name': '\u6807\u7b7e',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('views', models.IntegerField(default=0, verbose_name='\u6d4f\u89c8\u6570')),
                ('comnum', models.IntegerField(default=0, verbose_name='\u8bc4\u8bba\u6570')),
                ('top', models.BooleanField(default=False, verbose_name='\u662f\u5426\u7f6e\u9876')),
                ('sorttop', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5206\u7c7b\u7f6e\u9876')),
                ('hide', models.BooleanField(default=False, verbose_name='\u662f\u5426\u8f6c\u5165\u8349\u7a3f')),
                ('allow_remark', models.BooleanField(default=True, verbose_name='\u662f\u5426\u8bc4\u8bba')),
                ('digest', models.BooleanField(default=False, verbose_name='\u662f\u5426\u52a0\u7cbe')),
                ('password', models.CharField(max_length=50, verbose_name='\u6587\u7ae0\u52a0\u5bc6\u5bc6\u7801')),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name='\u52a0\u5165\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('author', models.ForeignKey(related_name='author', db_column=b'author', verbose_name='\u4f5c\u8005', to_field=b'username', to=settings.AUTH_USER_MODEL)),
                ('last_comuser', models.ForeignKey(related_name='last_comuser', db_column=b'last_comuser', verbose_name='\u6700\u540e\u56de\u590d\u7528\u6237', to_field=b'username', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='blog.Tag', verbose_name='\u6807\u7b7e')),
                ('topic_subclass', models.ForeignKey(verbose_name='\u4e00\u7ea7\u7c7b\u522b', to='blog.OneClass')),
            ],
            options={
                'ordering': ['-publish_time'],
                'verbose_name': '\u6587\u7ae0',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='tid',
            field=models.ForeignKey(related_name='tid', db_column=b'tid', verbose_name='\u6587\u7ae0ID', to='blog.Topic'),
        ),
    ]
