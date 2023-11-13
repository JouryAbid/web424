from django.shortcuts import render
from .models import product

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def login(request):
    return render(request, 'pages/login.html')

def shop(request):
    context = { 
        'products':product.objects.all()
    }
    return render(request, 'pages/shop.html', context)

def ProductDetails(request):
    return render(request, 'pages/ProductDetails.html')

def basket(request):
    return render(request, 'pages/basket.html')

def order(request):
    return render(request, 'pages/order.html')
