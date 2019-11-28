from . import views
from django.urls import path

urlpatterns = [
    path('show/', views.show),
    path('add_product/', views.product, name="add_product"),
    path('delete/<int:id>', views.destroy),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('raw_sql/', views.raw_sql),
]    