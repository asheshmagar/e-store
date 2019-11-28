from . import views
from django.urls import path

urlpatterns = [
    path('', views.add_to_wishlist, name='add_to_wishlist'),
]