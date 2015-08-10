# -*- coding: utf-8 -*-
import random


def set_cart_id(request):
    if request.session.get('cart_id', '') == '':
        request.session['cart_id'] = generate_cart_id()

    return request.session['cart_id']


def generate_cart_id():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    for a in range(50):
        cart_id += characters[random.randint(0, len(characters)-1)]

    return cart_id


def del_session_cart_id(request):

    if request.session.get('cart_id', '') != '':
        del request.session['cart_id']


def get_region(request):
    if request.session.get('region', '') == '':
        request.session['region'] = 'МОСКВА'

    return request.session['region']


def set_region(request):
    request.session['region'] = request.POST['region']

    return request.session['region']
