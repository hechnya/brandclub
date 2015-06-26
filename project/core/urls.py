# -*- coding: utf-8 -*-
#!/usr/bin/env python

from django.conf.urls import patterns, include, url

urlpatterns = patterns('project.core.views',

    # Главная страница
    url(r'^$', 'indexView'),
    url(r'^product/(?P<slug>[-\w]+)/$', 'product_view'),
    url(r'^page/(?P<slug>[-\w]+)/$', 'page_view') ,
    url(r'^article/(?P<id>[-\w]+)/$' , 'article_view'),
    url(r'^category/(?P<slug>[-\w]+)/$', 'category_view'),
    url(r'^products/$', 'products_view'),
    url(r'^article-add/$', 'article_add_view'),

    url(r'^account/$', 'account_view'),
    url(r'^order/(?P<id>[-\w]+)/$', 'order_view'),


    # url(r'^articles$', 'articlesView',
    #     {'template_name': 'core/articles.html'},
    #     name='articlesView'),
    #
    # url(r'^faq', 'faqView',
    #     {'template_name': 'core/faq.html'},
    #     name='faqView'),
    #
    # url(r'^about$', 'aboutView',
    #     {'template_name': 'core/about.html'},
    #     name='aboutView'),
    #
    # url(r'^contacts$', 'contactView',
    #     {'template_name': 'core/contact.html'},
    #     name='contactView'),
    #

    #
    # url(r'^article/(?P<slug>[-\w]+)/$', 'articleView',
    #     {'template_name':'core/article.html'},
    #     name='articleView'),
    #
    # # Просмотр категории
    # url(r'^category/(?P<category_slug>[-\w]+)/$', 'category_view',
    #    {'template_name':'category/category.html'},
    #    name='category_view'),
    #
    # url(r'^price/(?P<slug>[-\w]+)/$', 'price_view',
    #    {'template_name':'category/price.html'},
    #    name='price_view'),
)
