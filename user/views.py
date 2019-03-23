from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# from django.core.paginator import Paginator
from django.urls import reverse

from order.models import Order, OrderDetail
from user.forms import ProfileForm, UserForm
from .models import UserProfile
# from order.models import *
# from .models import ProductBrowser


# @login_required
# def profile(request):
#     user = request.user
#     if not hasattr(user, 'userprofile'):
#         user_profile = UserProfile()
#         user_profile.user = user
#
#     return render(request, 'account/profile.html', {'user': user})


@login_required
def myaccount(request):
    user = request.user

    if not hasattr(user, 'userprofile'):
        user_profile = UserProfile()
        user_profile.user = user
    else:
        user_profile = user.userprofile

    default_data1 = {'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}
    default_data2 = {'phone': user_profile.phone, 'zip': user_profile.zip, 'address': user_profile.address, }

    if request.method == "POST":
        pform = ProfileForm(request.POST)
        uform = UserForm(request.POST)

        if uform.is_valid():
            user.first_name = uform.cleaned_data['first_name']
            user.last_name = uform.cleaned_data['last_name']
            user.email = uform.cleaned_data['email']
            user.save()
            pform = ProfileForm(default_data2)

        if pform.is_valid():
            user_profile.phone = pform.cleaned_data['phone']
            user_profile.zip = pform.cleaned_data['zip']
            user_profile.address = pform.cleaned_data['address']
            user_profile.save()
            uform = UserForm(default_data1)

            return HttpResponseRedirect(reverse('user:myaccount'))
    else:
        uform = UserForm(default_data1)
        pform = ProfileForm(default_data2)

    user_id = request.user.id
    orders_list = Order.objects.filter(user_id=int(user_id)).order_by('-date')
    paginator = Paginator(orders_list, 2)
    page = paginator.page(1)

    context = {'uform': uform,
               'pform': pform,
               'user': user,
               'paginator': paginator,
               'page': page,
               'orders_list':orders_list,}

    return render(request, 'account/profile.html', context)


# @login_required
# def info(request):  # My Account
#     username = request.session.get('user_name')
#     user = User.objects.filter(username=username).first()
#     browsed_products = ProductBrowser.objects.filter(user=user).order_by("-browser_time")
#     product_list = []
#     if browsed_products:
#         product_list = [browsed_product.product for browsed_product in browsed_products]
#         explain = 'Recent viewed'
#     else:
#         explain = 'No recent browsed items'
#
#     context = {
#         'title': 'My Account',
#         'page_name': 1,
#         'user_phone': user.phone,
#         'user_address': user.address,
#         'user_name': username,
#         'product_list': product_list,
#         'explain': explain,
#     }
#     return render(request, 'account/profile.html', context)
#
#
# @login_required
# def order(request, index):
#     user_id = request.user.id
#     orders_list = Order.objects.filter(user_id=int(user_id)).order_by('-date')
#     paginator = Paginator(orders_list, 2)
#     page = paginator.page(int(index))
#     context = {
#         'paginator': paginator,
#         'page': page,
#         # 'orders_list':orders_list,
#         'title': "My Account",
#         'page_name': 1,
#     }
#     return render(request, 'account/profile.html', context)


# @login_required
# def order_detail(request, index):
#     user_id = request.user.id
#     orders_list = Order.objects.filter(user_id=int(user_id)).order_by('-date')
#     order_id = orders_list[index]
#     order_detail_list = OrderDetail.objects.filter(order_id=int(order_id))
#     paginator = Paginator(order_detail_list, 2)
#     page = paginator.page(1)
#     context = {
#         'paginator': paginator,
#         'page': page,
#         'title': "Order Detail",
#         'page_name': 1,
#     }
#     return render(request, 'account/myorders.html', context)
#
#
# @login_required
# def site(request):
#     user = User.objects.get(id=request.session['user_id'])
#     if request.method == "POST":
#         user.re_address = request.POST.get('re_address')
#         user.address = request.POST.get('address')
#         user.zip = request.POST.get('zip')
#         user.phone = request.POST.get('phone')
#         user.save()
#     context = {
#         'page_name': 1,
#         'title': 'My Account',
#         'user': user,
#     }
#     return render(request, 'account/myaddresses.html', context)
