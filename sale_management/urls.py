"""django_class URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from .views import OrderListView, EmployeeDetailView, EmployeeListView
from sale_management.views import product, employee, order
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/<pk>/', employee.DetailView.as_view(), name='detail'),
    path('employee/', employee.ListView.as_view(), name='listing'),
    # path('customer/', customer_list, name='customer_list'),
    # path('customer/<int:customer_id>/', customer_detail, name='customer_detail'),
    path('product/', product.ListView.as_view(), name='product_list'),
    path('product/<pk>', product.DetailView.as_view(), name='product_detail'),
    path('order/', order.ListView.as_view() , name='order_list'),
    path('order/<int:pk>', order.DetailView.as_view(), name='order_detail'),
]
