#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 19:45:58 2018

@author: yanis
"""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from registration import views

urlpatterns = [
    url(r'^registration/$', views.Ouruser_list),
    url(r'^registration/(?P<pk>[0-9]+)$', views.Ouruser_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)