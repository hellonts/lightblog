# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *
admin.autodiscover()


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('caption',)

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            'kindeditor-4.1.10/kindeditor-min.js',
            'kindeditor-4.1.10/lang/zh_CN.js',
            'kindeditor-4.1.10/config.js',
        )


admin.site.register(Topic,ArticleAdmin)
admin.site.register(OneClass)
admin.site.register(SecondClass)
admin.site.register(Comment)
admin.site.register(Options)
admin.site.register(Link)
admin.site.register(Tag)