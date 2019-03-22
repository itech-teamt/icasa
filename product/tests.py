from django.test import TestCase, Client
from .models import Product, Category


class ProductTest(TestCase):
    def setUp(self):
        cat1 = Category.objects.create(ctitle='fakeipad')
        cat2 = Category.objects.create(ctitle='fakeiphone')
        cat3 = Category.objects.create(ctitle='fakemac')
        cat4 = Category.objects.create(ctitle='fakewatch')
        cat5 = Category.objects.create(ctitle='fakeacc')
        cat6 = Category.objects.create(ctitle='fakeother')

        prod1 = Product.objects.create(name='ipad5', price=1000, stock=1000, image='/s.jpg', description='good', detail='doog', category=cat6)
        prod2 = Product.objects.create(name='ipad3', price=1000, stock=1000, image='/s.jpg', description='good',
                                       detail='doog', category=cat1)
        prod3 = Product.objects.create(name='ipad6', price=1000, stock=1000, image='/s.jpg', description='good',
                                       detail='doog', category=cat2)
        prod4 = Product.objects.create(name='ipadwww', price=1000, stock=1000, image='/s.jpg', description='good',
                                       detail='doog', category=cat3)
        prod5 = Product.objects.create(name='ipadqw', price=1000, stock=1000, image='/s.jpg', description='good',
                                       detail='doog', category=cat4)
        prod6 = Product.objects.create(name='ipadhhh', price=1000, stock=1000, image='/s.jpg', description='good',
                                       detail='doog', category=cat5)

    def test_product_models(self):
        pro = Product.objects.get(name='ipad5')
        self.assertEqual(pro.price, 1000)
        self.assertEqual(pro.stock, 1000)

    def test_index_view(self):
        c = Client()
        res = c.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'test')

    def test_detail_view(self):
        c = Client()
        res = c.get('/1/')
        self.assertEqual(res.status_code, 200)

    def test_about_view(self):
        c = Client()
        res = c.get('/1/')
        self.assertEqual(res.status_code, 200)
