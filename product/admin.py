# superuser: root 123123...
from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'ctitle']
    list_per_page = 10
    search_fields = ['ctitle']
    list_display_links = ['ctitle']


class ProductAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'name', 'click', 'price', 'image', 'stock', 'detail', 'description']
    list_editable = ['stock', 'detail', 'description']
    readonly_fields = ['click']
    search_fields = ['name', 'detail', 'description']
    list_display_links = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
