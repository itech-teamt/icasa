from django.contrib import admin

from .models import User, ProductBrowser


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "re_address", "address", "zip", "phone"]
    list_per_page = 5
    list_filter = ["username", "zip"]
    search_fields = ["username", "zip"]
    readonly_fields = ["username"]


class ProductBrowserAdmin(admin.ModelAdmin):
    list_display = ["user", "product"]
    list_per_page = 50
    list_filter = ["user__username", "product__name"]
    search_fields = ["user__username", "product__name"]
    readonly_fields = ["user", "product"]
    refresh_times = [3, 5]


admin.site.site_header = 'Admin System | iCasa'
admin.site.site_title = 'Admin System | iCasa'

admin.site.register(User, UserAdmin)
admin.site.register(ProductBrowser, ProductBrowserAdmin)
