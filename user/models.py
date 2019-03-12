from django.db import models
from datetime import datetime
from product.models import Product
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    address = models.CharField(max_length=100, default="", verbose_name="address", blank=True)
    zip = models.CharField(max_length=6, default="", verbose_name="zip code", blank=True)
    phone = models.CharField(max_length=11, default="", verbose_name="phone number", blank=True)

    def __str__(self):
        return self.user.__str__()


class ProductBrowser(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User ID")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product ID")
    browser_time = models.DateTimeField(default=datetime.now, verbose_name="Browse time")

    class Meta:
        verbose_name = "Browse history"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}Browse history{1}".format(self.user.username, self.product.name)
