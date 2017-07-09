# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160125_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secondclass',
            name='oneclass',
        ),
        migrations.AddField(
            model_name='oneclass',
            name='secondclass',
            field=models.ManyToManyField(to='blog.SecondClass', verbose_name='\u4e8c\u7ea7\u5206\u7c7b'),
        ),
    ]
