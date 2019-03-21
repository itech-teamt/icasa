from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse

from .models import *
from django.contrib.auth.decorators import login_required


@login_required
def user_cart(request):
    uid = request.user.id
    carts = Cart.objects.filter(user_id=uid)
    context = {
        'title': 'Cart',
        'page_name': 1,
        'carts': carts
    }
    # if it is an ajax submission we return a json
    if request.is_ajax():
        count = Cart.objects.filter(user_id=request.user.id).count()

        return JsonResponse({'count': count})
    else:
        return render(request, 'cart/cart.html', context)


@login_required
def add(request, gid, count):
    uid = request.user.id
    print(uid)
    gid, count = int(gid), int(count)
    # if the item is already in cart, we add the amount, otherwise we add it to cart
    carts = Cart.objects.filter(user_id=uid, product_id=gid)
    if len(carts) >= 1:
        cart = carts[0]
        cart.count = cart.count + count
    else:
        cart = Cart()
        cart.user_id = uid
        cart.product_id = gid
        cart.count = count
    cart.save()

    # if request.is_ajax():
    #     count = Cart.objects.filter(user_id=request.user.id).count()
    #
    #     return JsonResponse({'count': count})
    # else:
    return redirect(reverse("cart:cart"))


@login_required
def edit(request, cart_id, count):
    data = {}
    try:
        cart = Cart.objects.get(pk=int(cart_id))
        cart.count = int(count)
        cart.save()
        data['count'] = 0
    except Exception:
        data['count'] = count
    return JsonResponse(data)


@login_required
def delete(request, cart_id):
    data = {}
    try:
        cart = Cart.objects.get(pk=int(cart_id))
        cart.delete()
        data['ok'] = 1
    except Exception:
        data['ok'] = 0
    return JsonResponse(data)
