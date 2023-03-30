from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import *


class ProductListView(ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = 'products'

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        # get uncompleted order for current customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        # get all order items
        items = order.orderitem_set.all()
    else:
        #TODO displaying items and order for unlogged users
        items = []
        order = {'items_counter': 0, 'total_price': 0}
    
    context = {"items": items, "order": order}
    return render(request, 'shop/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'items_counter': 0, 'total_price': 0}
    
    context = {"items": items, "order": order}
    return render(request, 'shop/checkout.html', context)

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'