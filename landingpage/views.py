from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView


# Create your views here.
class Base(TemplateView):
    template_name = 'landingpage/pages/base.html'

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class Contact(TemplateView):
    template_name = 'contact.html'

class Products(TemplateView):
    template_name = 'products.html'