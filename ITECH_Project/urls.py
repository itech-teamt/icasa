"""ITECH_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^', include(('product.urls', 'product'), namespace='products')),
    url(r'^user/', include(('user.urls', 'user'), namespace='user')),
    url(r'^cart/', include(('cart.urls', 'cart'), namespace='cart')),
    url(r'^order/', include(('order.urls', 'order'), namespace='order')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^accounts/', include('allauth.urls')),
    # url(r'^auth/', include('social_django.urls', namespace='social')),
    # url(r'^login/(?P<backend>[^/]+){0}$'.format(extra), views.auth,
    #     name='begin'),
    # # 回调URL
    # url(r'^complete/(?P<backend>[^/]+){0}$'.format(extra), views.complete,
    #     name='complete'),
    # # disconnection
    # url(r'^disconnect/(?P<backend>[^/]+){0}$'.format(extra), views.disconnect,
    #     name='disconnect'),
    # url(r'^disconnect/(?P<backend>[^/]+)/(?P<association_id>\d+){0}$'
    #     .format(extra), views.disconnect, name='disconnect_individual'),
]
