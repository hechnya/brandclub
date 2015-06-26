# -*- coding: utf-8 -*-
#!/usr/bin/env python

from django.conf.urls import patterns, include, url

urlpatterns = patterns('authentication.views',

    # Главная страница
    url(r'logout/$', "logout_view"),
    url(r'login/$',"login_view"),



)
