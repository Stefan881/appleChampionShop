from django.urls import path
from . import views as stephen

urlpatterns = [
    path('', stephen.products, name='products-url'),
    path('add-products/', stephen.add_products, name='add-products-url'),
]
