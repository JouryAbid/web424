from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('shop', views.shop, name='shop'),
    path('product/<int:pro_id>/', views.productdetails, name='productdetails'),
    path('cart', views.cart, name='cart'),
    path('order', views.order, name='order'),
    path('search', views.search, name='search'),
]