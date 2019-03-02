from django.db import models

from user.models import User
from product.models import Product


class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Items in cart")
    count = models.IntegerField(verbose_name="")  # quantity

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username + '\'s Cart'
