# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='password',
            field=models.CharField(max_length=50, verbose_name='\u6587\u7ae0\u52a0\u5bc6\u5bc6\u7801', blank=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='\u6807\u7b7e', blank=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='topic_subclass',
            field=models.ForeignKey(verbose_name='\u4e00\u7ea7\u7c7b\u522b', to='blog.SecondClass'),
        ),
    ]
