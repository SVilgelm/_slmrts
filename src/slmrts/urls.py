# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
import views


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^order/{0,1}$', views.order),
    url(r'^order/(?P<bouquet_id>\d+)/{0,1}$', views.order),
)
