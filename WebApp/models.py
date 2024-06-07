from django.db import models

# Create your models here.

class ContactDb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=150,null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Subject = models.CharField(max_length=100,null=True,blank=True)
    Message = models.TextField(max_length=200,null=True,blank=True)

class RegistrationDb(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=150,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)

class CartDb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Product_name = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Total_Price = models.IntegerField(null=True,blank=True)