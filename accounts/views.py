from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect


def home(request):
    customers = Customer.objects.all().order_by("date_created")[0:5]
    orders = Order.objects.all().order_by("-date_created")
    last5_order = orders[0:5]
    orders_delivered = Order.objects.filter(status="Delivered")
    orders_pending = Order.objects.filter(status="Pending")
    context = {'customers': customers, 'orders': orders, 'orders_delivered': orders_delivered,
               'orders_pending': orders_pending, 'last_orders': last5_order}
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    Products = Product.objects.all().order_by("name")

    context = {'products': Products}
    return render(request, 'accounts/products.html', context)


def customer_info(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all

    context = {'customer': customer, 'orders': orders}
    return render(request, 'accounts/customer.html', context)


def new_customer(request):
    return render(request, 'accounts/new_customer.html')


def delete_view(request, pk):
    return render(request, )


def delete(request, pk):
    Customer.objects.get(id=pk).delete()
    return HttpResponseRedirect('/')


def update_view(request, pk):
    customer = Customer.objects.get(id=pk)
    context = {'customer': customer}
    return render(request, 'accounts/customerInfo.html', context)


def update_customer(request, pk):
    customer = Customer.objects.get(id=pk)

    customer_name = request.POST.get('customerName')
    customer_email = request.POST.get('customerEmail')
    customer_phone = request.POST.get('customerPhone')

    customer.name = customer_name
    customer.email = customer_email
    customer.phone = customer_phone
    customer.save()

    return HttpResponseRedirect('/')


def new_customer_view(request):
    return render(request, 'accounts/new_customer.html')


def new_customer(request):
    customer_name = request.POST.get('customerName')
    customer_email = request.POST.get('customerEmail')
    customer_phone = request.POST.get('customerPhone')

    Customer.objects.create(name=customer_name, email=customer_email, phone=customer_phone)

    return HttpResponseRedirect('/all_customer')


def new_order_view(request):
    customers = Customer.objects.all()
    orders_status = Order.STATUS
    products_list = Product.objects.all()

    context = {'customers': customers, 'orders_status': orders_status, 'products': products_list}
    return render(request, 'accounts/new_order.html', context)


def new_order(request):
    order_customer = Customer.objects.get(name=request.GET.get('order_customer'))
    order_product = Product.objects.get(name=request.GET.get('order_product'))
    order_status = request.GET.get('order_status')

    Order.objects.create(customer=order_customer, product=order_product, status=order_status)
    return HttpResponseRedirect('/')


def new_product(request):
    if request.method == 'POST':
        tag1 = Tag.objects.get(id=1)
        tag2 = Tag.objects.get(id=2)
        description = "Description for the product"
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        product_category = request.POST.get('category')
        print("PRODUCT TAG IS: ", product_category)
        product = Product.objects.create(name=product_name, price=product_price, category=product_category,
                                         description=description)
        tag1.products.add(product)
        tag2.products.add(product)
        return HttpResponseRedirect('/')
    return render(request, 'accounts/new_product.html')


def customers_list(request):
    customers = Customer.objects.all().order_by("date_created")
    context = {'customers': customers}
    return render(request, 'accounts/customers.html', context)
