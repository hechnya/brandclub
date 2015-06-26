from django.contrib import admin
from project.core.models import Product, Article, Page , ProductImage ,ArticleImage ,PageImage, Category

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Article)
admin.site.register(Page)
admin.site.register(ProductImage)
admin.site.register(ArticleImage)
admin.site.register(PageImage)
admin.site.register(Category)