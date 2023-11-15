from django.shortcuts import render, redirect
from django.contrib import messages
from pages.models import product
from .models import Order, OrderDetailes

# Create your views here.

def add_to_cart(request):
   if 'pro_id' in request.GET and 'quantity' in request.GET and 'price' in request.GET and request.user.is_authenticated and not request.user.is_anonymous:
        pro_id = request.GET['pro_id']
        qty = request.GET['quantity']

        order = Order.objects.all().filter(user=request.user,
                                           is_finished=False)

        if not product.objects.all().filter(id=pro_id).exists():
            return redirect('shop')

        pro = product.objects.get(id=pro_id)

        if order:
            old_order = Order.objects.get(user=request.user, is_finished=False)
            if OrderDetailes.objects.all().filter(order=old_order, product=pro).exists():
                orderdetails = OrderDetailes.objects.get(
                    order=old_order, product=pro)
                orderdetails.quantity += int(qty)
                orderdetails.save()
            else:
                orderdetails = OrderDetailes.objects.create(product=pro,
                                                           order=old_order, price=pro.price, quantity=qty)
            messages.success(request, 'added to existing cart')

        else:
            new_order = Order()
            new_order.user = request.user
            new_order.is_finished = False
            new_order.save()
            orderdetails = OrderDetailes.objects.create(product=pro,
                                                       order=new_order, price=pro.price, quantity=qty)
            messages.success(request, 'added to new cart')

        return redirect('shop' + request.GET['pro_id'])
   else:
        if 'proـid' in request.GET:
            messages.error(request, 'You must be logged in')
            return redirect('shop' + request. GET['pro_id'])
        else:
            return redirect('index')


def cart(request):
    context = None
    if request.user.is_authenticated and not request.user.is_anonymous:
        if Order.objects.all().filter(user=request.user, is_finished=False):
            order = Order.objects.get(user=request.user, is_finished=False)
            orderdetails = OrderDetailes.objects.all().filter(order=order)
            total = 0
            for sub in orderdetails:
                total += sub.price * sub.quantity
            context = {
                'order': order,
                'orderdetails': orderdetails,
                'total': total,
            }
    return render(request, 'pages/cart.html', context)



def remove_from_cart(request, orderdetails_id):
    if request.user.is_authenticated and not request.user.is_anonymous and orderdetails_id:
        orderdetails = OrderDetailes.objects.get(id=orderdetails_id)
        if orderdetails.order.user.id == request.user.id:
            orderdetails.delete()
    return redirect('cart')

def sub_qty(request, orderdetails_id):
    if request.user.is_authenticated and not request.user.is_anonymous and orderdetails_id:
        orderdetails = OrderDetailes.objects.get(id=orderdetails_id)
        if orderdetails.order.user.id == request.user.id:
            if orderdetails.quantity > 1:
                orderdetails.quantity -= 1
                orderdetails.save()
    return redirect('cart')

def add_qty(request, orderdetails_id):
    if request.user.is_authenticated and not request.user.is_anonymous and orderdetails_id:
        orderdetails = OrderDetailes.objects.get(id=orderdetails_id)
        if orderdetails.order.user.id == request.user.id:
            orderdetails.quantity += 1
            orderdetails.save()
    return redirect('cart')


