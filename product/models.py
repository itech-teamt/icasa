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
    isDelete = models.BooleanField(default=False)
    name = models.CharField(max_length=20, verbose_name="Product name", unique=True)
    image = models.ImageField(upload_to='product', verbose_name="product image path")
    image2 = models.ImageField(upload_to='product', null=True, verbose_name="product image2 path")
    image3 = models.ImageField(upload_to='product', null=True, verbose_name="product image3 path")
    image4 = models.ImageField(upload_to='product', null=True,verbose_name="product image4 path")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Product price")
    click = models.IntegerField(default=0, verbose_name="the number of clicks of a product")
    description = models.CharField(max_length=200, verbose_name="product description")
    stock = models.IntegerField(verbose_name="products in stock")
    detail = HTMLField(max_length=3000, verbose_name="product details")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="product category")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
