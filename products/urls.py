from django.urls import path
from . import views as stephen

urlpatterns = [
    path('', stephen.products, name='products-url'),
    path('add-products/', stephen.add_products, name='add-products-url'),
    path('delete/<id>', stephen.delete, name='delete-url'),
    path('update/<id>', stephen.update_products, name='update-url'),
    path('pay/<id>', stephen.pay, name="pay-url"),
]
