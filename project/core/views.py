# -*- coding: utf-8 -*-
from django.shortcuts import render
from project.core.models import Product, Article, ProductImage, ArticleImage, PageImage, Page, Category, Slide, ProductParametr
from project.cart.models import CartItem, Order, Delivery
from django.shortcuts import render_to_response
from django.template import RequestContext
from project.cart import cart
from django.http import HttpResponseRedirect, HttpResponse, Http404
import json
from django.shortcuts import get_object_or_404


from project.settings import STATIC_ROOT

# Page = {}

def add_to_cart(request):
    id = request.POST['id']
    product = Product.objects.get(id=id)
    cart_id = cart.set_cart_id(request)
    parametr_price = request.POST['parametr_price']
    parametr = ProductParametr.objects.get(product=product, price=parametr_price)

    try:
        tmp_item = CartItem.objects.get(cart_id=cart_id, product=product, parametr=parametr)
        tmp_item.count += int(request.POST['count'])
        tmp_item.save()
    except:
        cartItem = CartItem()
        cartItem.parametr = parametr
        cartItem.product = product
        cartItem.count = request.POST['count']
        cartItem.cart_id = cart_id
        cartItem.save()


def indexView(request, template_name='core/index.html'):

    products = Product.objects.all()
    # new_test = STATIC_ROOT
    slides = Slide.objects.all()

    for product in products:
        product.list_parametr = ProductParametr.objects.filter(product=product)

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

    # product = Product.objects.get(slug=slug)
    product = get_object_or_404(Product, slug=slug)
    category = product.category.all()[0]
    request.breadcrumbs([(category.name, category.url()), (product.name, request.path_info)])
    list_parametr = ProductParametr.objects.filter(product=product)
    parametr = ProductParametr.objects.get(product=product, is_main=True)
    list_image = ProductImage.objects.filter(product=product)

    if request.method == 'POST':
        if "parametr_weight" in request.POST:
            parametr = ProductParametr.objects.get(product=product, weight=request.POST['parametr_weight'])
        else:
            add_to_cart(request)

    # tmp_post = request.POST

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def page_view(request, slug, template_name="core/page.html" ):

    page = get_object_or_404(Page, slug=slug)
    request.breadcrumbs(page.name, request.path_info)
    try:
        page.pageimage = PageImage.objects.filter(page=page)[0]
    except:
        pass

    articles = Article.objects.all()

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def article_view(request, id, template_name="core/article.html"):

    article = Article.objects.get(id=id)
    try:
        article.articleimage = ArticleImage.objects.filter(article=article)[0]
    except:
        pass
    request.breadcrumbs(article.name, request.path_info)

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def articles_view(request, template_name="core/articles.html"):
    articles = Article.objects.all()

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def category_view(request, slug, template_name="core/category.html"):

    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    request.breadcrumbs(category.name, request.path_info)

    for product in products:
        product.list_parametr = ProductParametr.objects.filter(product=product)

    if request.method == 'POST':
        add_to_cart(request)


    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def products_view(request, template_name="core/products.html"):

    products = Product.objects.all()
    request.breadcrumbs("Продукты", request.path_info)

    for product in products:
        product.list_parametr = ProductParametr.objects.filter(product=product)

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
    if request.user.is_authenticated() and request.user.is_staff:
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


def ajax_cart(request):
    add_to_cart(request)
    global_quantity = 0
    product = Product.objects.get(id=request.POST["id"])
    data = json.dumps({
        "global_quantity": global_quantity,
        "product_name": u"%s" % product.name,
        "product_image": u"/media/%s" % product.get_image().image,
        "description": u"%s" % product.description,
        "weight": u"%s" % product.paramemtr()
    })
    return HttpResponse(data, content_type="application/json")


def success_views(request, template_name="robokassa/success.html"):

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def fail_views(request, template_name="robokassa/fail.html"):

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def mail_view(request, template_name="core/email.html"):
    cart_id = "V7I2OqalpUAf1MnKa2q2Km9DxyM2QHYOqVyZsOhyA5VgfyIYt7"
    order = Order.objects.get(cart_id=cart_id)
    cart_items = CartItem.objects.filter(cart_id=cart_id)
    name = request.user.get_full_name()
    price = order.total_price()
    absolut_link = 'http://127.0.0.1:8000'

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def search_view(request, template_name="core/search.html"):
    products = Product.objects.filter(name__icontains=request.GET['text'])

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))





