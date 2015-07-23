# -*- coding: utf-8 -*-
from django.contrib import admin
from project.core.models import Product, Article, Page, ProductImage, ArticleImage, PageImage, Category, Slide, ProductParametr


class ProductImageAdmin(admin.StackedInline):
    """Добавление изображений продукта"""
    model = ProductImage
    extra = 0

class ProductParametrAdmin(admin.StackedInline):
    """Добавление изображений продукта"""
    model = ProductParametr
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductParametrAdmin, ProductImageAdmin]
    prepopulated_fields = {'slug': ('name',), }


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Article)
admin.site.register(Page)
admin.site.register(ProductImage)
admin.site.register(ArticleImage)
admin.site.register(PageImage)
admin.site.register(Category)
admin.site.register(Slide)
admin.site.register(ProductParametr)


