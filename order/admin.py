from django.contrib import admin

from .models import OrderDetail, Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ["id", "user", "date", "total_price", "address"]
    list_per_page = 5
    list_filter = ["user", "date", "address"]
    search_fields = ["user__username"]
    ordering = ["-date"]


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):

    list_display = ["product", "order", "price", "count"]
    list_per_page = 5
    list_filter = ["product"]
