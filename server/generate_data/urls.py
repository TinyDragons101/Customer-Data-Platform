from django.urls import path
from . import views

urlpatterns = [
    path('generate_data/customers', views.generate_customers, name='generate_customers'),
    path('generate_data/products', views.generate_products, name='generate_products'),
    path('generate_data/orders', views.generate_orders, name='generate_orders'),
]
