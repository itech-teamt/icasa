from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# from django.core.paginator import Paginator
from django.urls import reverse

from order.models import Order
from user.forms import ProfileForm
from .models import UserProfile
# from order.models import *
# from .models import ProductBrowser


@login_required
def profile(request):
    user = request.user
    if not hasattr(user, 'userprofile'):
        user_profile = UserProfile()
        user_profile.user = user

    return render(request, 'account/profile.html', {'user': user})


@login_required
def profile_update(request):
    user = request.user
    if not hasattr(user, 'userprofile'):
        user_profile = UserProfile()
        user_profile.user = user
    else:
        user_profile = user.userprofile

    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            user_profile.phone = form.cleaned_data['phone']
            user_profile.zip = form.cleaned_data['zip']
            user_profile.address = form.cleaned_data['address']
            user_profile.save()

            return HttpResponseRedirect(reverse('user:profile'))
    else:
        default_data = {'first_name': user.first_name, 'last_name': user.last_name, 'phone': user_profile.phone, 'zip': user_profile.zip, 'address':user_profile.address}
        form = ProfileForm(default_data)

    return render(request, 'account/profile_update.html', {'form': form, 'user': user})


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
@login_required
def order(request, index):
    user_id = request.user.id
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
    return render(request, 'account/myorders.html', context)
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
