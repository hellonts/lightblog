# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160125_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic_subclass',
            field=models.ForeignKey(verbose_name='\u4e8c\u7ea7\u7c7b\u522b', to='blog.SecondClass'),
        ),
    ]
