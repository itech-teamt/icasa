from django.db import models
from product.models import Product
from user.models import User


class Order(models.Model):  # the entire order
    id = models.CharField(max_length=20, primary_key=True, verbose_name="order id")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="order user")
    date = models.DateTimeField(auto_now=True, verbose_name="date")
    has_payed = models.BooleanField(default=False, verbose_name="payment status")
    total_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="total price")
    address = models.CharField(max_length=150, verbose_name="order address")

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.user.username + "\'s order at" + str(self.date)


# currently unavailable：real payment & delivery information
class OrderDetail(models.Model):  # the order of an item in the entire order

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="product")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="order")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="product price")
    count = models.IntegerField(verbose_name="quantity")

    class Meta:
        verbose_name = "Order detail"
        verbose_name_plural = "Order details"

    def __str__(self):
        return "{0}(quantity:{1})".format(self.product.name, self.count)
