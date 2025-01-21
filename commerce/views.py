from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product

def home (requset):
    products = Product.objects.filter(is_available=True)
    context={
        'products':products
    }
    return render(requset, 'home.html', context)