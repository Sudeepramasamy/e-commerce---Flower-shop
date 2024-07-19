
from django.db import models
import datetime
import os
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


# Create your models here.
def getFileName(request,filname):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filname)
    return os.path.join('uploads/',new_filename)

class Signin(models.Model):
    Name=models.CharField(max_length=20,default="")
    PhoneNumber=models.IntegerField(default="")
    Gmail=models.CharField(max_length=20,default="")
    Password=models.CharField(max_length=20,default="")

class Catagory(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    description=models.TextField(max_length=150,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Products(models.Model):
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    price=models.IntegerField(null=False,blank=False)
    description=models.TextField(max_length=150,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-trending")
    created_at=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    @property
    def total_amount(self):
      return self.product_qty*self.product.price
  
class Order(models.Model):
    Name=models.CharField(max_length=50,default="")
    Email=models.CharField(max_length=20,default="")
    Address=models.CharField(max_length=100,default="")  
    Pincode=models.IntegerField(default="")
    City=models.CharField(max_length=50,default="")
    
    
    



    
     