from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def shop(request):
    # prod_category = request.GET.get('category')
    # if prod_category!='1':
    #     products = Product.get_all_products_by_categoryid(prod_category)
    # else:
    #     products = Product.get_all_products
    # context = {
    #     'products': products,
    #     'category':prod_category
    # }
    # return render(request, "shop/shop.html", context)
    return HttpResponse("Django deployed.")

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
