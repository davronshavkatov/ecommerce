from django.shortcuts import render,get_object_or_404
from category.models import Category
from .models import Product
# Create your views here.   
def store(request, category_slug=None):
    if category_slug == None:
        products = Product.objects.filter(is_available=True)
    else:
        categoryies = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(is_available=True, category=categoryies)
    context={
        'products':products,
        'product_count': products.count()
    }
    return render (request, 'store.html', context)

def product_detail(request, category_slug, product_slug):
    product = get_object_or_404(Product, slug=product_slug, category__slug=category_slug)
    context = {
        'product':product
    }
    return render (request, 'product_detail.html', context)
