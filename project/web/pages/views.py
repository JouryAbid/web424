from django.shortcuts import get_object_or_404, render
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

def productdetails(request, pro_id):
    context= {
        'pro': get_object_or_404(product, pk= pro_id)
      }
    pass
    return render(request, 'pages/productdetails.html', context)

def cart(request):
    return render(request, 'pages/cart.html')

def order(request):
    return render(request, 'pages/order.html')

def search(request):
    return render(request, 'pages/search.html')
