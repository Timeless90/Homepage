from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Stock

# Create your views here.
class BaseDashboard(TemplateView):
    template_name = 'base_dashboard.html'


class StockListView(ListView):
    model = Stock
    template_name = 'base_dashboard.html'
    context_object_name = 'stocks'