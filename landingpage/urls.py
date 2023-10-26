from .views import Base, Home, About, Contact, Products
from django.urls import path

urlpatterns = [
    path('', Base.as_view(), name='base'),
    path('home/', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('products/', Products.as_view(), name='products'),
    ]