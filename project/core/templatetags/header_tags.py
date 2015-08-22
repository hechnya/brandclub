# -*- coding: utf-8 -*-
from django import template
register = template.Library()
from project.core.models import Category
from project.cart.models import CartInfoHelper
from project.cart import cart
from yandex_maps import api

def top_menu(context, request):

    cart_info = CartInfoHelper()
    cart_info.cart_id = cart.set_cart_id(request)
    cart_info.cart_total_price_helper()

    # cart_ifo = cart_info

    return {
        'user': request.user,
        'request': request,
        'cart_info': cart_info
    }
register.inclusion_tag('core/tags/top_menu.html', takes_context=True)(top_menu)


def category(context, request):

    return {'nodes': Category.objects.all()}

register.inclusion_tag('core/tags/category.html', takes_context=True)(category)


def cart_menu(context, request):
    cart_info = CartInfoHelper()
    cart_info.cart_id = cart.set_cart_id(request)
    cart_info.cart_total_price_helper()

    return {'cart_info': cart_info}

register.inclusion_tag('core/tags/cart_menu.html', takes_context=True)(cart_menu)