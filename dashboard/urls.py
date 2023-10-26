from .views import BaseDashboard
from django.urls import path

urlpatterns = [
    path('', BaseDashboard.as_view(), name='base'),
    ]