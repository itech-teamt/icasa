from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
from django.test import TestCase,Client
from .models import User, UserProfile, Product
from .views import *
from django.http import HttpResponse, HttpRequest
import os

# first run all the tests of django-allauth (an integrated account management app that we are using)
os.system("python manage.py test allauth.tests")

# Create your tests here.
class UserTest(TestCase):
    def setUp(self):
        user1 = User.objects.create(first_name='john', last_name='doe', email='qq@qq.com', username='johndoe', password='jjjjj123456')
        userprofile1 = UserProfile.objects.create(user=user1, address="Glasgow", zip='G128QQ', phone='123456')
        s = Site.objects.get_or_create(domain='example.com')[0]
        s.domain = 'localhost:8000'
        s.name = 'iCasa'
        s.save()
        sapp = SocialApp.objects.get_or_create(provider="facebook", name="iCasa", client_id="2338256373071830", secret="e2777dd08b0da339f1f137e7a7891567")[0]
        sapp.sites.add(s)
        sapp.save()

    def test_user_models(self):
        user = User.objects.get(username='johndoe')
        self.assertEqual(user.last_name, 'doe')
        self.assertEqual(user.email, 'qq@qq.com')
        self.assertEqual(user.password, 'jjjjj123456')
        userprofile = UserProfile.objects.get(user=user)
        self.assertEqual(userprofile.address, "Glasgow")
        self.assertEqual(userprofile.zip, 'G128QQ')
        self.assertEqual(userprofile.phone, '123456')

    def test_user_views(self):
        c = Client()
        # test if we can access the signup page
        res = c.get('/accounts/signup/')
        self.assertEqual(res.status_code, 200)

        # we are not logged in so the status code should not be 200
        res2 = c.get('/user/myaccount')
        self.assertNotEqual(res2.status_code, 200)

    # test if we can access the myaccount page
    def test_myaccount_view(self):
        u = User.objects.get(username='johndoe')
        request = HttpRequest()
        request.user = u  # the page requires logging in so we add a user to the request
        res = myaccount(request)
        self.assertEqual(res.status_code, 200)

