from django.db import models
from tinymce.models import HTMLField

class Category(models.Model):
    # categories of products
    isDelete = models.BooleanField(default=False)
    ctitle = models.CharField(max_length=20, verbose_name="Category title")

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.ctitle


class Product(models.Model):
    # the class for products
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="product category")
    isDelete = models.BooleanField(default=False)
    name = models.CharField(max_length=20, verbose_name="Product name", unique=True)
    image = models.ImageField(upload_to='product', verbose_name="product image path")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Product price")
#   weight = models.CharField(max_length=20, default='500g', verbose_name="product ")
    click = models.IntegerField(default=0, verbose_name="the number of clicks of a product")
    description = models.CharField(max_length=200, verbose_name="product description")
    stock = models.IntegerField(verbose_name="products in stock")
    detail = HTMLField(max_length=200, verbose_name="product details")
    # adv = models.BooleanField(default=False) # we recommend or not

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
