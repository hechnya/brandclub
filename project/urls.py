from django.conf import os
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from project.sitemap import ProductSitemap, CategorySitemap, IndexSitemap, PageSitemap, ArticleSitemap

sitemaps = {
    "products": ProductSitemap,
    "category": CategorySitemap,
    "index": IndexSitemap,
    "page": PageSitemap,
    "article": ArticleSitemap,

}
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^', include('project.core.urls')),
    url(r'^', include('project.cart.urls')),
    url(r'^', include('authentication.urls')),
    url(r'^robokassa/fail/$', 'project.core.views.fail_views'),
    url(r'^robokassa/success/$', 'project.core.views.success_views'),
    url(r'^robokassa/', include('robokassa.urls')),
    url(r'^robots.txt$', 'project.core.views.robots_view'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),


]

if settings.DEBUG:
    urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
        )

# if settings.DEBUG404:
#     urlpatterns += patterns('',
#         (r'^static/(?P<path>.*)$', 'django.views.static.serve',
#          {'document_root': os.path.join(os.path.dirname(__file__), 'static')} ),
#     )