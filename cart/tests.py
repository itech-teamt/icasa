from django.http import HttpRequest
from django.test import TestCase, Client

from user.models import UserProfile
from .models import Cart, Product, User
from product.models import Category
from .views import add, delete, edit


# Create your tests here.
class cartTest(TestCase):
    def setUp(self):
        user1 = User.objects.create(first_name='john', last_name='doe', email='qq@qq.com', username='johndoe',
                                    password='jjjjj123456')
        userprofile1 = UserProfile.objects.create(user=user1, address="Glasgow", zip='G128QQ', phone='123456')
        category1 = Category.objects.create(ctitle='iphone')
        product1 = Product.objects.create(name='iphone3gs', stock=2000, price=200, category=category1)
        product2 = Product.objects.create(name='iphone2', stock=2000, price=200, category=category1)
        cart1 = Cart.objects.create(user=user1, product=product1, count=1)

    def test_cart_models(self):
        result = Cart.objects.get(count=1)
        self.assertEqual(result.user.first_name, 'john')
        self.assertEqual(result.user.last_name, 'doe')
        self.assertEqual(result.user.email, 'qq@qq.com')
        self.assertEqual(result.user.username, 'johndoe')
        self.assertEqual(result.user.password, 'jjjjj123456')

    # test adding a product in cart
    def test_cart_add_view(self):
        user2 = User.objects.create(first_name='john', last_name='doe', email='qq@qq.com', username='johndoe2',
                                    password='jjjjj123456')

        p = Product.objects.get(name='iphone2')
        request = HttpRequest()
        request.user = user2  # the page requires logging in so we add a user to the request
        res = add(request, p.id, 3)
        cart = Cart.objects.get(user=user2)
        self.assertEqual(cart.count, 3)
        self.assertEqual(cart.product.name, 'iphone2')

    def test_cart_remove_view(self):
        u = User.objects.get(username='johndoe')
        request = HttpRequest()
        request.user = u
        res = delete(request, 1)
        try:
            cart = Cart.objects.get(pk=1) # the cart has been deleted. we try to get it but it should not be get
        except:
            cart = None

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'ok')  # the request has been processed
        self.assertTrue(cart is None, "the cart has been deleted")

    def test_cart_edit_view(self):
        u = User.objects.get(username='johndoe')
        request = HttpRequest()
        request.user = u
        res = edit(request, 1, 3)
        cart = Cart.objects.get(pk=1)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(cart.count, 3)
