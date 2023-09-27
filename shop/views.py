from django.shortcuts import render
from .models import Product

def shop(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, "shop/shop.html", context)

def category(request):
    return render(request, "shop/category.html")

def offers(request):
    return render(request, "shop/offers.html")

def gallery(request):
    return render(request, "shop/gallery.html")

def blogs(request):
    return render(request, "shop/blogs.html")

def profile(request):
    return render(request, "shop/profile.html")
