from django.core.paginator import Paginator
from django.shortcuts import render

from cart.models import Cart
from user.models import ProductBrowser
from .models import Product, Category
from django.contrib.auth.decorators import login_required


def index(request):
    # show 4 hottest and 4 latest products of each category
    caregorylist = Category.objects.all()

    cat0 = caregorylist[0].product_set.order_by('-id')[0:4]  # sort by create time
    cat01 = caregorylist[0].product_set.order_by('-click')[0:4]  # sort by number of clicks
    cat1 = caregorylist[1].product_set.order_by('-id')[0:4]
    cat11 = caregorylist[1].product_set.order_by('-click')[0:4]
    cat2 = caregorylist[2].product_set.order_by('-id')[0:4]
    cat21 = caregorylist[2].product_set.order_by('-click')[0:4]
    cat3 = caregorylist[3].product_set.order_by('-id')[0:4]
    cat31 = caregorylist[3].product_set.order_by('-click')[0:4]
    cat4 = caregorylist[4].product_set.order_by('-id')[0:4]
    cat41 = caregorylist[4].product_set.order_by('-click')[0:4]
    cat5 = caregorylist[5].product_set.order_by('-id')[0:4]
    cat51 = caregorylist[5].product_set.order_by('-click')[0:4]

    cart_num = 0

    # if request.session.has_key('user_id'):
    if not request.user.id is None:
        user_id = request.user.id
        cart_num = Cart.objects.filter(user_id=int(user_id)).count()

    context = {
        'title': 'Home | ITECH_Project',
        'cart_num': cart_num,
        'guest_cart': 1,
        'cat0': cat0, 'cat01': cat01,
        'cat1': cat1, 'cat11': cat11,
        'cat2': cat2, 'cat21': cat21,
        'cat3': cat3, 'cat31': cat31,
        'cat4': cat4, 'cat41': cat41,
        'cat5': cat5, 'cat51': cat51,
    }

    return render(request, 'product/index.html', context)


@login_required
def product_list(request, cid, pindex, sort):
    # cid：category id;  pindex：page index; sort：method of sorting
    category = Category.objects.get(pk=int(cid))

    # search category by pk
    news = category.product_set.order_by('-id')[0:2]
    # list.html-left side bar
    products_list = []
    # list-middle
    cart_num, guest_cart = 0, 0
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        if user_id:
            guest_cart = 1
            cart_num = Cart.objects.filter(user_id=int(user_id)).count

    if sort == '1':  # sort by newest
        products_list = Product.objects.filter(category_id=int(cid)).order_by('-id')
    elif sort == '2':  # sort by price
        products_list = Product.objects.filter(category_id=int(cid)).order_by('-price')
    elif sort == '3':  # sort by clicks
        products_list = Product.objects.filter(category_id=int(cid)).order_by('-click')

    # make an object of paginator
    paginator = Paginator(products_list, 3)
    # return a paginator containing relative information
    page = paginator.page(int(pindex))
    context = {
        'title': 'Product list',
        'guest_cart': guest_cart,
        'cart_num': cart_num,
        'page': page,
        'paginator': paginator,
        'category': category,
        'sort': sort,  # sorting method
        'news': news,
    }
    return render(request, 'product/list.html', context)


def detail(request, pid):
    product_id = pid
    product = Product.objects.get(pk=int(product_id))
    product.click = product.click + 1
    product.save()

    news = product.category.product_set.order_by('-id')[0:2]
    context = {
        'title': product.category.ctitle,
        'guest_cart': 1,
        'cart_num': cart_count(request),
        'product': product,
        'news': news,
        'id': product_id,
    }
    response = render(request, 'product/detail.html', context)

    if not request.user.id is None:
        user_id = request.user.id
        try:
            browsed_product = ProductBrowser.objects.get(user_id=int(user_id), product_id=int(product_id))
        except Exception:
            browsed_product = None
        if browsed_product:
            from datetime import datetime
            browsed_product.browser_time = datetime.now()
            browsed_product.save()
        else:
            ProductBrowser.objects.create(user_id=int(user_id), product_id=int(product_id))
            browsed_product = ProductBrowser.objects.filter(user_id=int(user_id))
            browsed_product_count = browsed_product.count()
            if browsed_product_count > 5:
                ordered_products = browsed_product.order_by("-browser_time")
                for _ in ordered_products[5:]:
                    _.delete()
    return response


def cart_count(request):
    if not request.user.id is None:
        return Cart.objects.filter(user_id=request.user.id).count()
    else:
        return 0


@login_required
def search(request):

    from django.db.models import Q
    search_keywords = request.GET.get('q', '')
    pindex = request.GET.get('pindex', 1)
    search_status = True
    cart_num, guest_cart = 0, 0

    if search_keywords:
        products_list = Product.objects.filter(
            Q(name__icontains=search_keywords) |
            Q(detail__icontains=search_keywords) |
            Q(description__icontains=search_keywords)).order_by("click")
    else:
        search_status = False
        products_list = Product.objects.all().order_by("click")

    # paginator = Paginator(products_list,9)
    # page = paginator.page(1)

    context = {
        'title': 'Search list',
        'search_status': search_status,
        'guest_cart': guest_cart,
        'cart_num': cart_num,
        'products_list': products_list,
        # 'page': page,
        # 'paginator': paginator,
        'q':search_keywords,
    }
    return render(request, 'product/search.html', context)


def about(request):
    return render(request, 'about.html')
