from django.shortcuts import render
from .models import Product, Tag
from django.views.generic import ListView

class AllProductsView(ListView):
    model = Product
    template_name = 'all-products.html'
    context_object_name = 'products'

class MaleProductsView(ListView):
    model = Product
    template_name = 'male-products.html'
    context_object_name = 'products'

class FemaleProductsView(ListView):
    model = Product
    template_name = 'female-products.html'
    context_object_name = 'products'
