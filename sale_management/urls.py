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
from .views import detail, listing, customer_detail, customer_list, order_detail, product_detail, product_list, order_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/<int:employee_id>/', detail, name='detail'),
    path('employee/', listing, name='listing'),
    path('customer/', customer_list, name='customer_list'),
    path('customer/<int:customer_id>/', customer_detail, name='customer_detail'),
    path('product/', product_list, name='product_list'),
    path('product/<int:product_id>', product_detail, name='product_detail'),
    path('order/', order_list, name='order_list'),
    path('order/<int:order_id>', order_detail, name='order_detail'),
]
