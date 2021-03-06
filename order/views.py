from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

from datetime import datetime
from decimal import Decimal

from .models import Order, OrderDetail
from cart.models import Cart
from user.models import User
from django.contrib.auth.decorators import login_required


@login_required
def order(request):
    uid = request.user.id
    user = User.objects.get(id=uid)
    cart_ids = request.GET.getlist('cart_id')
    carts = []
    total_price = 0
    for product_id in cart_ids:
        cart = Cart.objects.get(id=product_id)
        carts.append(cart)
        total_price = total_price + float(cart.count) * float(cart.product.price)

    total_price = float('%0.2f' % total_price)
    trans_cost = 0  # delivery is free for now. maybe in the future we will raise the delivery fee so we make this variable.
    total_trans_price = trans_cost + total_price
    if not hasattr(request.user, 'userprofile'):
        address = 0
    else:
        if not hasattr(user.userprofile, 'address'):
            address = 0
        else:
            address = 1

    context = {
        'address':address,
        'title': 'Submit order',
        'page_name': 1,
        'user': user,
        'carts': carts,
        'total_price': float('%0.2f' % total_price),
        'trans_cost': trans_cost,
        'total_trans_price': total_trans_price,
        # 'value':value
    }
    return render(request, 'order/order.html', context)


@login_required
# @transaction.atomic()
def order_handle(request):
    user_id = request.user.id
    # if not hasattr(request.user, 'userprofile'):
    #     return
    tran_id = transaction.savepoint()
    cart_ids = request.POST.get('cart_ids')

    data = {}
    try:
        order_info = Order()  # make a new order object
        now = datetime.now()
        order_info.id = '%s%d' % (now.strftime('%Y%m%d%H%M%S'), user_id)  # concatenating an ID of order
        order_info.date = now  # create time of the order
        order_info.user_id = int(user_id)  # user id of the order
        order_info.total_price = Decimal(request.POST.get('total_price'))  # get total price
        order_info.save()  # SAVE ORDER

        for cart_id in cart_ids.split(','):
            cart = Cart.objects.get(pk=cart_id)  # get a cart object
            order_detail = OrderDetail()
            order_detail.order = order_info
            product = cart.product  # a product in cart
            if cart.count <= product.stock:
                product.stock = product.stock - cart.count
                product.save()
                order_detail.product = product
                order_detail.price = product.price
                order_detail.count = cart.count
                order_detail.save()
                cart.delete()  # delete current cart
            else:  # cancel order
                transaction.savepoint_rollback(tran_id)
                return HttpResponse('Insufficient stock')
        data['ok'] = 1
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print("%s" % e)
        print('Failed to submit order')
        transaction.savepoint_rollback(tran_id)  # cancel the whole process when a part has a problem
    return JsonResponse(data)


# We are not including real payment function in this project
@login_required
def pay(request):
    pass
