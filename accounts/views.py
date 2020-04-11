from django.shortcuts import render
from .models import *


def home(request):
    customers = Customer.objects.all().order_by("-date_created")
    orders = Order.objects.all().order_by("-date_created")
    orders_delivered = Order.objects.filter(status="Delivered")
    orders_pending = Order.objects.filter(status="Pending")
    context = {'customers': customers, 'orders': orders, 'orders_delivered': orders_delivered,
               'orders_pending': orders_pending}
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    return render(request, 'accounts/products.html')


def customer(request):
    return render(request, 'accounts/customer.html')
