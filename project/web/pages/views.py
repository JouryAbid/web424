from django.shortcuts import render
from .models import product

# Create your views here.
def index(request):
    context = { 
        'products':product.objects.all()
    }
    return render(request, 'pages/index.html', context)

def login(request):
    return render(request, 'pages/signin.html')

def shop(request):
    name = None
    pro = product.objects.all()

    if 'searchname' in request.GET:
        name = request.GET['searchname']
        if name:
            pro = pro.filter(name__icontains= name)
            
    context = { 
        'products': pro,
    }
    return render(request, 'pages/shop.html', context)

def ProductDetails(request):
    return render(request, 'pages/ProductDetails.html')

def basket(request):
    return render(request, 'pages/basket.html')

def order(request):
    return render(request, 'pages/order.html')

def search(request):
    return render(request, 'pages/search.html')
