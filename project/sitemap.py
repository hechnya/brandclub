# -*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from project.core.models import Product, Category, Page, Article


class ProductSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Product.objects.all()

    # def lastmod(self, obj):
    #     return obj.pub_date

class CategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Category.objects.all()

class IndexSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1

    def items(self):
        return ["index"]

    def location(self, item):
        return "/"

class PageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Page.objects.all()

class ArticleSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Article.objects.all()
