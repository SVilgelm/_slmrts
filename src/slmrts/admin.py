# -*- coding: utf-8 -*-
from django.contrib import admin
from imagekit.admin import AdminThumbnail
from models import Bouquet, Photo


class PhotoInline(admin.TabularInline):
    model = Photo


class BouquetAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'created', )
    list_filter = ('cost', )
    search_fields = ('name', 'cost',)
    readonly_fields = ('created',)
    inlines = (PhotoInline, )


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('admin_thumbnail', 'bouquet')
    list_filter = ('bouquet', )
    search_fields = ('bouquet',)
    admin_thumbnail = AdminThumbnail(image_field='small_image')


admin.site.register(Bouquet, BouquetAdmin)
admin.site.register(Photo, PhotoAdmin)
