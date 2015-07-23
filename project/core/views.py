# -*- coding: utf-8 -*-
from django.shortcuts import render
from project.core.models import Product, Article, ProductImage, ArticleImage, PageImage, Page, Category, Slide, ProductParametr
from project.cart.models import CartItem, Order, Delivery
from django.shortcuts import render_to_response
from django.template import RequestContext
from project.cart import cart
from django.http import HttpResponseRedirect
from project import settings

from project.settings import STATIC_ROOT

# Page = {}

def add_to_cart(request):
    id = request.POST['id']
    product = Product.objects.get(id=id)
    cart_id = cart.set_cart_id(request)
    id_parametr = request.POST['id_parametr']

    try:
        tmp_item = CartItem.objects.get(cart_id=cart_id, product=product)
        tmp_item.count += int(request.POST['count'])
        tmp_item.save()
    except:
        cartItem = CartItem()
        cartItem.parametr = ProductParametr.objects.get(id=id_parametr)
        cartItem.product = product
        cartItem.count = request.POST['count']
        cartItem.cart_id = cart_id
        cartItem.save()


def indexView(request, template_name='core/index.html'):
    dir_test = settings

    products = Product.objects.all()
    # new_test = STATIC_ROOT
    slides = Slide.objects.all()

    if request.method == 'POST':
        add_to_cart(request)

    articles = Article.objects.all()
    for art in articles:
        try:
            art.image = ArticleImage.objects.filter(article=art)[0]
        except:
            pass

    pages = Page.objects.all()
    for pag in pages:
        try:
            pag.image = PageImage.objects.filter(page=pag)
            pag.image = pag.image[0]
        except:
            pass


    return render_to_response(template_name, locals(), context_instance=RequestContext(request))
    # return render(request, 'core/index.html', {'products': products ,'articles' : articles })


def product_view(request, slug, template_name="core/product.html"):

    product = Product.objects.get(slug=slug)
    category = product.category.all()[0]
    request.breadcrumbs([(category.name, category.url()), (product.name, request.path_info)])
    list_parametr = ProductParametr.objects.filter(product=product)
    parametr = ProductParametr.objects.get(product=product, is_main=True)

    if request.method == 'POST':
        if "parametr_weight" in request.POST:
            parametr = ProductParametr.objects.get(product=product, weight=request.POST['parametr_weight'])
        else:
            add_to_cart(request)

    # tmp_post = request.POST

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def page_view(request, slug, template_name="core/page.html" ):

    page = Page.objects.get(slug=slug)
    request.breadcrumbs(page.name, request.path_info)
    try:
        page.pageimage = PageImage.objects.filter(page=page)[0]
    except:
        pass

    articles = Article.objects.all()

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def article_view(request, id, template_name="core/article.html"):

    article = Article.objects.get(id=id)
    article.articleimage = ArticleImage.objects.filter(article=article)[0]
    request.breadcrumbs(article.name, request.path_info)

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def category_view(request, slug, template_name="core/category.html"):

    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    request.breadcrumbs(category.name, request.path_info)

    if request.method == 'POST':
        add_to_cart(request)


    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def products_view(request, template_name="core/products.html"):

    products = Product.objects.all()
    request.breadcrumbs("Продукты", request.path_info)

    if request.method == 'POST':
        add_to_cart(request)


    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def article_add_view(request, template_name="core/article_add.html"):
    user = request.user
    if request.method == 'POST':

        name = request.POST['name']
        text = request.POST['text']

        article = Article()
        article.name = name
        article.text = text
        article.save()

        image  = ArticleImage()
        image.article = article
        file = request.FILES['file']
        image.save()


    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def account_view(request, template_name="core/account.html"):
    if request.user.is_authenticated():
        orders = Order.objects.all()

        for order in orders:
            order.items = order.get_all_cart_items()

            for item in order.items:
                item.name = item.product.name
    else:
        # request.session['last_url'] = request.path
        return HttpResponseRedirect('/login/')


    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def order_view(request, id, template_name="core/order.html"):
    order = Order.objects.get(id=id)
    delivery = Delivery.objects.get(cart_id=order.cart_id)


    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def robots_view(request):
    return render_to_response("robots.txt", content_type="text/plain")







