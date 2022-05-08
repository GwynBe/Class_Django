from msilib.schema import ListView
from re import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from sale_management.models import Employee, Customer, Product, Order, OrderDetail
from django.template import loader
from django.views import generic

# Create your views here.

def detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, template_name='employee/detail.html', context={
        'employee': employee
    })

class EmployeeDetailView(generic.DetailView):
    template_name = "employee/detail.html"
    model = Employee

def listing(request):
    latest_employee_list = Employee.objects.order_by('-created_at')
    # template = loader.get_template('index.html')
    return render(request, template_name='employee/index.html', context={
        'latest_employee_list': latest_employee_list
    })

class EmployeeListView(generic.ListView):
    template_name = "employee/index.html"
    context_object_name = 'latest_employee_list'

    def get_queryset(self):
        return Order.objects.order_by('id')

def customer_list(request):
    customers = Customer.objects.order_by('id')
    return render(request, template_name='customer/list.html', context={
        'customers': customers
    })

def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, template_name='customer/detail.html', context={
        'customer': customer
    })

def product_list(request):
    products = Product.objects.order_by('name')
    return render(request, template_name='product/list.html', context={
        'products': products
    })
    
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, template_name='product/detail.html', context={
        'product': product
    })

def order_list(request):
    orders = Order.objects.order_by('id')
    return render(request, template_name='order/list.html', context={
        'orders': orders
    })

def order_detail(request, order_id):
    order_detail = OrderDetail.objects.filter(order_id=order_id)
    return render(request, template_name='order/detail.html', context={
        'order_detail': order_detail
    })

