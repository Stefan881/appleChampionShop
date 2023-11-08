from django.urls import path
from . import views as stephen

urlpatterns = [
    path('register/', stephen.register, name='registration-url'),

]
