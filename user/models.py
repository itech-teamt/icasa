from django.db import models

from datetime import datetime

from product.models import Product


class User(models.Model):

    username = models.CharField(max_length=20, verbose_name="username", unique=True)
    password = models.CharField(max_length=40, verbose_name="password", blank=False)
    email = models.EmailField(verbose_name="email", unique=True)
    re_address = models.CharField(max_length=20, default="", verbose_name="recipient address")
    address = models.CharField(max_length=100, default="", verbose_name="address")
    zip = models.CharField(max_length=6, default="", verbose_name="zip code")
    phone = models.CharField(max_length=11, default="", verbose_name="phone number")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


class ProductBrowser(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User ID")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product ID")
    browser_time = models.DateTimeField(default=datetime.now, verbose_name="Browse time")

    class Meta:
        verbose_name = "Browse history"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}Browse history{1}".format(self.user.username, self.product.name)
