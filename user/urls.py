
from django.conf.urls import url

from .views import *

app_name = 'user'

urlpatterns = [
    # url(r'^register/$', register, name="register"),
    # url(r'^register_handle/$', register_handle, name="register_handle"),
    # url(r'^register_exist/$', register_exist, name="register_exist"),
    # url(r'^login/$', login, name="login"),
    # url(r'^login_handle/$', login_handle, name="login_handle"),
    url(r'^myaccount/$', myaccount, name="myaccount"),
    # url(r'^profile/update/$', profile_update, name="profile_update"),
    # url(r'^order/(\d+)$', order_detail, name="order_detail"),
    # url(r'^address/$', site, name="address"),
    # url(r'^logout/$', logout, name="logout"),
]
