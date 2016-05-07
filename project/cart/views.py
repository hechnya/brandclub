# -*- coding: utf-8 -*-
from django.shortcuts import render
from project.cart.models import CartItem, Order, CartInfoHelper, Delivery
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from project.cart import cart, delivery
from authentication.models import Account
from django.contrib.auth import login, logout
from authentication.forms import AccountForm, PureAccountForm, DeliveryForm
from project.settings import ADMIN_EMAIL
from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import HttpResponseRedirect, HttpResponse
from robokassa.forms import RobokassaForm
from robokassa.signals import result_received
import json
from django.template.loader import render_to_string

from project.settings import ABSOLUT_LINK

from django.contrib.sessions.models import Session


def cart_view(request, template_name="cart/cart.html"):

    cart_id = cart.set_cart_id(request)
    region = cart.get_region(request)

    user = request.user
    form = AccountForm()
    delivery_form = DeliveryForm()

    if user.is_authenticated():
        if region == 'МОСКВА':
            initial_region = user.city
        else:
            initial_region = region
        data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'zip': user.zip,
            'city': initial_region,
            'address': user.address,
            'phone': user.phone
        }
        pureForm = PureAccountForm(initial=data)

    cart_items = CartItem.objects.filter(cart_id=cart_id)

    cart_info = CartInfoHelper()
    cart_info.cart_id = cart_id

    if request.method == 'POST' and "checkout" in request.POST:
        if user.is_authenticated():
            postdata = request.POST.copy()
            pureForm = PureAccountForm(postdata)

            if pureForm.is_valid():
                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.zip = request.POST['zip']
                user.city = request.POST['city']
                user.address = request.POST['address']
                user.phone = request.POST['phone']
                user.save()

        else:
            postdata = request.POST.copy()
            form = AccountForm(postdata)

            if form.is_valid():
                email = request.POST['email']
                password = request.POST['password']
                username = request.POST['username']
                user = Account.objects.create_user(email, password=password, username=username)
                login(request, user)
                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.zip = request.POST['zip']
                user.city = request.POST['city']
                user.address = request.POST['address']
                user.phone = request.POST['phone']
                user.save()

        order = Order()
        order.user = user
        order.cart_id = cart_id
        order.save()

        url = '/confirmation?cart_id=%s' % request.session['cart_id']
        cart.del_session_cart_id(request)

        return HttpResponseRedirect(url)

    elif request.method == "POST" and "delete" in request.POST:
        tmp_id = request.POST['id']
        tmp_item = CartItem.objects.get(id=tmp_id)
        tmp_item.delete()

    elif request.method == "POST" and "change_count" in request.POST:
        id = int(request.POST['id'])
        tmp_count = request.POST['count']
        tmp_item = CartItem.objects.get(id=id)
        tmp_item.count = tmp_count
        tmp_item.save()

    # elif request.method == "POST" and "post_city" in request.POST:
    #     region = request.POST["region"]
    #     weight = 0
    #     for item in cart_items:
    #         weight = weight + item.parametr.weight * item.count
    #
    #     cart_info.delivery_price = delivery.calculate_delivery(weight, region)
    #     cart_info.get_total_price()
    #
    #     try:
    #         delivery_item = Delivery.objects.get(cart_id=cart_id)
    #         delivery_item.city = region
    #         delivery_item.price = cart_info.delivery_price
    #         delivery_item.save()
    #     except:
    #         delivery_item = Delivery()
    #         delivery_item.city = region
    #         delivery_item.price = cart_info.delivery_price
    #         delivery_item.cart_id = cart_id
    #         delivery_item.save()






        # user = request.user
        # cart_id = cart.set_cart_id(request)
        #
        # try:
        #     tmp_item = CartItem.objects.get(user=user, product=product)
        #     tmp_item.count += int(request.POST['count'])
        #     tmp_item.save()
        # except:
        #     cartItem = CartItem()
        #     cartItem.product = product
        #     # cartItem.user = user
        #     cartItem.count = request.POST['count']
        #     cartItem.cart_id = cart_id
        #     cartItem.save()

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def confirmation_view(request, template_name="cart/confirmation.html"):
    # получить  пользователя
    # нужно получить заказ
    # нужно получить доставку
    if request.user.is_authenticated():

        if request.method == 'GET' and "cart_id" in request.GET:
            cart_id = request.GET['cart_id']
            user = request.user

            order = Order.objects.get(cart_id=cart_id)

            form = RobokassaForm(initial={
                       'OutSum': order.total_price(),
                       'InvId': order.id,
                   })

            order.save()
            subject = u'заявка от %s' % order.user.first_name
            message = u'Номер заказа: %s \n Имя: %s \n телефон: %s' % (order.id, order.user.last_name, order.user.phone)
            send_mail(subject, message, 'halturin77@gmail.com', [ADMIN_EMAIL], fail_silently=False)
            # subject = u'Пользователь не оплатил %s' % order.user.first_name
            # message = u'Номер заказа: %s \n Имя: %s \n телефон: %s' % (order.id, order.user.last_name, order.user.phone)
            # send_mail(subject, message, 'halturin77@gmail.com', [ADMIN_EMAIL], fail_silently=False)
        # else:
        #     if request.method == 'POST' and "mail" in request.POST:
        #         cart_id = request.POST['cart_id']
        #         order = Order.objects.get(cart_id=cart_id)
        #         items = CartItem.objects.filter(cart_id=cart_id)
        #         context_dict = {
        #             'name': request.user.get_full_name(),
        #             'cart_items': items,
        #             'price': order.total_price(),
        #         }
        #
        #
        #         subject = u'Супер письмо'
        #         message = render_to_string(
        #             'core/email.html', context_dict)
        #
        #         from_email = 'test@mail.ru'
        #         to = "hechnya@mail.ru"
        #         msg = EmailMultiAlternatives(subject, message, from_email, [to])
        #         msg.content_subtype = "html"
        #         msg.send()
        #     return HttpResponseRedirect('/')

    else:
        return HttpResponseRedirect('/login')


    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def payment_received(sender, **kwargs):
    """обрабатываем сигнал оплаты от платежной системы"""
    order = Order.objects.get(id=kwargs['InvId'])
    order.is_paid = True
    order.save()

    subject = u'заявка от %s' % order.user.first_name
    message = u'Номер заказа: %s \n Имя: %s \n телефон: %s' % (order.id, order.user.last_name, order.user.phone)
    send_mail(subject, message, 'halturin77@gmail.com', [ADMIN_EMAIL], fail_silently=False)

    subject = u'Заказ на kastoreum.ru%s' % order.user.first_name
    message = u'Номер заказа %s \n Спасибо, %s! \n Ваша заявка принята! ' % (order.id, order.user.first_name,)
    send_mail(subject, message, 'halturin77@gmail.com', [order.user.email], fail_silently=False)

    cart_id = order.cart_id
    items = CartItem.objects.filter(cart_id=cart_id)
    context_dict = {
        'name': order.user.get_full_name(),
        'cart_items': items,
        'price': order.total_price(),
        'absolut_link': ABSOLUT_LINK
    }


    subject = u'Супер письмо'
    message = render_to_string(
        'core/email.html', context_dict)

    from_email = 'test@mail.ru'
    to = "hechnya@mail.ru"
    msg = EmailMultiAlternatives(subject, message, from_email, [to])
    msg.content_subtype = "html"
    msg.send()
    
result_received.connect(payment_received)


def ajax_delivery(request):

    cart_id = cart.set_cart_id(request)
    cart_items = CartItem.objects.filter(cart_id=cart_id)
    region = cart.set_region(request)
    weight = 0
    cart_info = CartInfoHelper()
    cart_info.cart_id = cart_id
    for item in cart_items:
        weight = weight + item.parametr.weight * item.count

    cart_info.delivery_price = delivery.calculate_delivery(weight, region)
    cart_info.get_total_price()

    try:
        delivery_item = Delivery.objects.get(cart_id=cart_id)
        delivery_item.city = region
        delivery_item.price = cart_info.delivery_price
        delivery_item.save()
    except:
        delivery_item = Delivery()
        delivery_item.city = region
        delivery_item.price = cart_info.delivery_price
        delivery_item.cart_id = cart_id
        delivery_item.save()

    data = json.dumps({
        "region": region,
        "delivery_price": cart_info.delivery_price,
        "item_price": cart_info.item_price,
        "total_price": cart_info.total_price,
        })
    return HttpResponse(data, content_type="application/json")



