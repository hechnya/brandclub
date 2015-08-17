# -*- coding: utf-8 -*-
#!/usr/bin/env python

from django.conf.urls import patterns, include, url

urlpatterns = patterns('project.cart.views',

    # Главная страница
    url(r'cart/$', "cart_view"),
    url(r'confirmation/$', "confirmation_view"),
    url(r'^ajax-delivery/$', 'ajax_delivery'),

)
