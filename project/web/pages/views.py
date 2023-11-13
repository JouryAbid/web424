from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def login(request):
    return render(request, 'pages/login.html')

def shop(request):
    return render(request, 'pages/shop.html')

def ProductDetails(request):
    return render(request, 'pages/ProductDetails.html')

def basket(request):
    return render(request, 'pages/basket.html')

def order(request):
    return render(request, 'pages/order.html')
