"""store URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from . import api
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('layout/', include('mainApp.urls')),
    path('about/', include('about.urls')),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('cart/', include('cart.urls')),
    path('shop/', include('shop.urls')),
    path('checkout/', include('checkout.urls')),
    path('product_detail/', include('product_detail.urls')),
    path('order_complete/', include('order_complete.urls')),
    path('add_to_wishlist/', include('add_to_wishlist.urls')),
    path('login/', include('login.urls')),
    path('product/', include('product.urls')),
    path('profile/', include('user_profile.urls')),
    path('api/v1/', include(api.router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
