from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('shop', views.shop, name='shop'),
    path('ProductDetails', views.ProductDetails, name='ProductDetails'),
    path('basket', views.basket, name='basket'),
    path('order', views.order, name='order'),
]