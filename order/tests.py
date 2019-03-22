from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import TestCase

from cart.views import add
from product.models import Product, Category
from user.models import UserProfile
from .models import Order, OrderDetail
from .views import order, order_handle


# Create your tests here.
class OrderTests(TestCase):
    def setUp(self):
        user1 = User.objects.create(first_name='john', last_name='doe', email='qq@qq.com', username='johndoe',
                                    password='jjjjj123456')
        # userprofile1 = UserProfile.objects.create(user=user1, address="Glasgow", zip='G128QQ', phone='123456')
        cat6 = Category.objects.create(ctitle='fakeother')

        prod1 = Product.objects.create(name='ipad5', price=1000, stock=1000, image='/s.jpg', description='good', detail='doog', category=cat6)
        order1 = Order.objects.create(id="001", user=user1, address="glasgow", total_price=2000)
        detail1 = OrderDetail.objects.create(order=order1, price=1000, count=2, product=prod1)

    def test_order_models(self):
        od = OrderDetail.objects.get(pk=1)
        o = Order.objects.get(id="001")
        self.assertEqual(od.count, 2)
        self.assertEqual(od.order.address, o.address)
        self.assertEqual(od.price*od.count, o.total_price)
        self.assertEqual(o.address, "glasgow")

    def test_order_view(self):
        u = User.objects.get(username='johndoe')
        request = HttpRequest()
        request.user = u
        res = order(request)
        self.assertEqual(res.status_code, 200, "request processed successfully")

    def test_order_handle_view(self):
        u = User.objects.get(username='johndoe')
        p = Product.objects.get(name='ipad5')
        request = HttpRequest()
        request.user = u
        request.POST['total_price'] = 1000
        request.POST['cart_ids'] = "1"
        add(request, p.id, 3)
        res = order_handle(request)
        self.assertEqual(res.status_code, 200, "request processed successfully")

