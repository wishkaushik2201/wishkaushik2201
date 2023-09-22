from email.policy import default
from django.db import models
import datetime

from django.forms import CharField

# from Libraryapp.lib_memb.views import subscription

class registraion(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    email=models.EmailField(max_length=254)
    password1=models.CharField(max_length=255)
    DateofBirth=models.CharField(max_length=20)
    mobileno=models.CharField(max_length=20)
    # subscription=models.BooleanField(default=False)



# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class product(models.Model):
    bookname=models.CharField(max_length=50)
    image=models.ImageField(upload_to='upload/product')
    authorname=models.CharField(max_length=50)
    description=models.CharField(max_length=255, default="good")
    category=models.ForeignKey(category,on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.name
# class subs(models.Model):
#     product=models.ForeignKey(product,on_delete=models.CASCADE)
#     customer=models.ForeignKey(registraion,on_delete=models.CASCADE)
#     price=models.IntegerField()
#     address=models.CharField(max_length=50,default="", blank=True)
#     phone=models.IntegerField(default=1)
#     date=models.DateField(default=datetime.datetime.today)
#     status=models.BooleanField(default=False)
#     def __str__(self):
#         return self.address

class wishlist(models.Model):
    bookname=models.CharField(max_length=50)
    image=models.ImageField(upload_to='upload/product')
    authorname=models.CharField(max_length=50)
    description=models.CharField(max_length=255, default="good")
    category=models.ForeignKey(category,on_delete=models.CASCADE,default=1)
