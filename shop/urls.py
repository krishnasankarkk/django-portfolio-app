from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('products', views.shop, name='shop'),
    path('categories', views.category, name='category'),
    path('offers', views.offers, name='offers'),
    path('gallery', views.gallery, name='gallery'),
    path('blogs', views.blogs, name='blogs'),
    path('profile', views.profile, name='profile'),
]