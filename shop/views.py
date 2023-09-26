from django.shortcuts import render
from .models import Product

def shop(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, "shop/shop.html", context)
