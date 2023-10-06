from django.contrib import admin
from .models import Product, Category, Menu, ChildMenu 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "description", "price"]

admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(ChildMenu)
