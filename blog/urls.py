#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import url
from django.contrib import admin
from blog import views
from django.views.static import serve
from blog_s19 import settings
import re

from blog import views

urlpatterns = [
    # # 个人站点页面
    # url(r'^(?P<username>\w+)/$', views.home_site),
    # # 归档
    # url(r'^(?P<username>\w+)/(?P<condition>cate|tag|date)/(?P<param>.*)', views.home_site),
    # # 文章详细页
    # url(r'^(?P<username>\w+)/articles/(?P<article_id>\d+)', views.article_detail),
    # # 后台管理
    # url(r'^backend/$', views.backend),
    # url(r'^backend/add_article/$', views.add_article),
    # # 点赞
    # url(r'^up_down/$', views.up_down),
    # # 评论
    # url(r'^comment/$', views.comment),

    # 后台管理
    url(r'^backend/$', views.backend),
    url(r'^backend/add_article/$', views.add_article),
    # 点赞
    url(r'^up_down/$', views.up_down),
    # 评论
    url(r'^comment/$', views.comment),
    # 个人站点页面
    url(r'^(?P<username>\w+)/$', views.home_site),

    # 归档
    url(r'^(?P<username>\w+)/(?P<condition>cate|tag|date)/(?P<param>.*)', views.home_site),
    # 文章详细页
    url(r'^(?P<username>\w+)/articles/(?P<article_id>\d+)', views.article_detail),



]
