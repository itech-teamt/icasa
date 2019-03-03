from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.core.paginator import Paginator
from django.http import JsonResponse

from hashlib import sha1

from .models import ProductBrowser
from . import decorator
from order.models import *


def register(request):

    context = {
        'title': 'Register',
    }
    return render(request, 'user/register.html', context)


def register_handle(request):

    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    confirm_pwd = request.POST.get('confirm_pwd')
    email = request.POST.get('email')

    # the two passwords should be equal
    if password != confirm_pwd:
        return redirect('/user/register/')
    # encrypt the password
    s1 = sha1()
    s1.update(password.encode('utf8'))
    encrypted_pwd = s1.hexdigest()

    # make object
    User.objects.create(username=username,
                           password=encrypted_pwd,
                           email=email)
    # successful registration
    context = {
        'title': 'Login',
        'username': username,
    }
    return render(request, 'user/login.html', context)


def register_exist(request):
    username = request.GET.get('username')
    count = User.objects.filter(username=username).count()
    return JsonResponse({'count': count})


def login(request):
    username = request.COOKIES.get('username', '')
    context = {
        'title': 'Login',
        'error_name': 0,
        'error_pwd': 0,
        'username': username,
    }
    return render(request, 'user/login.html', context)


def login_handle(request):  # not an ajax submission
    # receive request
    username = request.POST.get('username')
    password = request.POST.get('pwd')
    remember = request.POST.get('remember', 0)
    users = User.objects.filter(username=username)
    if len(users) == 1:
        s1 = sha1()
        s1.update(password.encode('utf8'))
        if s1.hexdigest() == users[0].password:
            url = request.COOKIES.get('url', '/')
            red = HttpResponseRedirect(url)
            # remember username or not
            if remember != 0:
                red.set_cookie('username', username)
            else:
                red.set_cookie('username', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = username
            return red
        else:
            context = {
                'title': 'Username login',
                'error_name': 0,
                'error_pwd': 1,
                'username': username,
                'password': password,
            }
            return render(request, 'user/login.html', context)
    else:
        context = {
            'title': 'Username login',
            'error_name': 1,
            'error_pwd': 0,
            'username': username,
            'password': password,
        }
        return render(request, 'user/login.html', context)


@decorator.login
def logout(request):  # User logout
    request.session.flush()  # clear all session
    return redirect(reverse("product:index"))


@decorator.login
def info(request):  # My Account
    username = request.session.get('user_name')
    user = User.objects.filter(username=username).first()
    browsed_products = ProductBrowser.objects.filter(user=user).order_by("-browser_time")
    product_list = []
    if browsed_products:
        product_list = [browsed_product.product for browsed_product in browsed_products]  # 从浏览商品记录中取出浏览商品
        explain = 'Recent viewed'
    else:
        explain = 'No recent browsed items'

    context = {
        'title': 'My Account',
        'page_name': 1,
        'user_phone': user.phone,
        'user_address': user.address,
        'user_name': username,
        'product_list': product_list,
        'explain': explain,
    }
    return render(request, 'user/account_info.html', context)


@decorator.login
def order(request, index):
    user_id = request.session['user_id']
    orders_list = Order.objects.filter(user_id=int(user_id)).order_by('-date')
    paginator = Paginator(orders_list, 2)
    page = paginator.page(int(index))
    context = {
        'paginator': paginator,
        'page': page,
        # 'orders_list':orders_list,
        'title': "My Account",
        'page_name': 1,
    }
    return render(request, 'user/myorders.html', context)


@decorator.login
def site(request):
    user = User.objects.get(id=request.session['user_id'])
    if request.method == "POST":
        user.re_address = request.POST.get('re_address')
        user.address = request.POST.get('address')
        user.zip = request.POST.get('zip')
        user.phone = request.POST.get('phone')
        user.save()
    context = {
        'page_name': 1,
        'title': 'My Account',
        'user': user,
    }
    return render(request, 'user/myaddresses.html', context)


