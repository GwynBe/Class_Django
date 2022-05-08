from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CreatedAbstractModel(models.Model):
    created_at = models.DateTimeField(
        blank=True, null=True, auto_now_add=True, 
        db_index=True)
    created_by = models.ForeignKey(
        User,
        blank=True, null=True, on_delete=models.SET_NULL,
        related_name = '%(app_label)s_%(class)s_created_by'
    )
    class Meta:
        abstract = True


class ModifiedAbstractModel(models.Model):
    modified_by = models.ForeignKey(
        User,
        blank=True, null=True, on_delete=models.SET_NULL,
        related_name = '%(app_label)s_%(class)s_updated_by'
    )
    modified_at = models.DateTimeField(
        blank=True, null=True, auto_now=True,
        db_index=True
    )

    class Meta:
        abstract = True


class TrackingAbstractModel(CreatedAbstractModel, ModifiedAbstractModel):
    class Meta:
        abstract = True


class Employee(TrackingAbstractModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    dob = models.DateField(null=True) #date of birth
    def __str__(self):
        return f'{self.name}'


class Customer(TrackingAbstractModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.name} - {self.phone}'


class Product(TrackingAbstractModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    def __str__(self):
        return f'{self.name} - {self.price} - {self.stock}'


class Order(TrackingAbstractModel):
    id = models.AutoField(primary_key=True)
    ordered_at = models.DateTimeField()
    delivery_at = models.DateField(null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.id} - {self.employee} - {self.customer} - {self.ordered_at} - {self.delivery_at}'


class OrderDetail(TrackingAbstractModel):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    def __str__(self):
        return f'{self.id} - {self.order} - {self.product} - {self.quantity}'
    
    @property
    def subtotal(self):
        return self.quantity * self.price
