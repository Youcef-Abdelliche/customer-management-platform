from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<int:pk>/', views.customer_info, name='customer'),
    path('newcustomer/', views.new_customer, name='new_customer'),
    path('customer/<int:pk>/delete/', views.delete, name='delete'),
    path('customer/<int:pk>/update/', views.update_view, name='update'),
    path('customer/<int:pk>/update_customer/', views.update_customer, name='update_customer'),
    path('new_customer/', views.new_customer_view, name='new_customer_view'),
    path('newcustomer/', views.new_customer, name='new_customer'),
    path('new_order_view/', views.new_order_view, name='new_order_view'),
    path('new_order/', views.new_order, name='new_order'),
]
