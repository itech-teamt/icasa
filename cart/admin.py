from django.contrib import admin

from .models import Cart


@admin.register(Cart)
class CartInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'count']
    list_per_page = 5
    list_filter = ['user', 'product', 'count']
    search_fields = ['user_username', 'product__name']
    readonly_fields = ['user', 'product', 'count']
# added