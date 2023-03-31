from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from django.http import JsonResponse
import json
from .models import *


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cart_items_counter = order.items_counter
    else:
        # logic for guest user
        order = {'items_counter': 0, 'total_price': 0}
        cart_items_counter = order['items_counter']

    products = Product.objects.all()
    context = {'products': products, 'cart_items_counter': cart_items_counter}
    return render(request, 'shop/home.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        # get uncompleted order for current customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        # get all order items
        items = order.orderitem_set.all()
        cart_items_counter = order.items_counter
    else:
        #TODO displaying items and order for unlogged users
        items = []
        order = {'items_counter': 0, 'total_price': 0}
        cart_items_counter = order['items_counter']
    
    context = {"items": items, "order": order, 'cart_items_counter': cart_items_counter}
    return render(request, 'shop/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items_counter = order.items_counter
    else:
        items = []
        order = {'items_counter': 0, 'total_price': 0}
        cart_items_counter = order['items_counter']
    
    context = {"items": items, "order": order, 'cart_items_counter': cart_items_counter}
    return render(request, 'shop/checkout.html', context)

def update_item(request):
    # this view work only for logged user!

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    # get order attached to the customer
    order, created = Order.objects.get_or_create(customer=customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def product_detail(request, id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cart_items_counter = order.items_counter
    else:
        # logic for guest user
        order = {'items_counter': 0, 'total_price': 0}
        cart_items_counter = order['items_counter']

    product = get_object_or_404(Product, id=id)
    context = {'product': product, 'cart_items_counter': cart_items_counter}
    return render(request, 'shop/product_detail.html', context=context)
