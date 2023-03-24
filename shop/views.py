from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'