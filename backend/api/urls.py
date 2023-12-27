from django.urls import path, include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('dev', views.DevelopmentModelList)
routers.register('customers', views.CustomerList)


urlpatterns = [
    path('', include(routers.urls))
]