from django.conf.urls import url

from . import views

app_name = 'product'

urlpatterns = [
    url('^$', views.index, name="index"),
    url('^list(\d+)_(\d+)_(\d+)/$', views.product_list, name="product_list"),
    url('^(\d+)/$', views.detail, name="detail"),
    url(r'^search/', views.search, name="search"),
]
