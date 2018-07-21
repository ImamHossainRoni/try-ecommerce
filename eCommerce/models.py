from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    Category_Name = models.CharField(max_length=80)

    def __str__(self):
        return self.Category_Name


class Brand(models.Model):
    Brand_Name = models.CharField(max_length=80)

    def __str__(self):
        return self.Brand_Name


class Product(models.Model):
    Product_Name = models.CharField(max_length=80)
    Product_info = models.TextField(null = True)
    Image = models.FileField( null = True)  #work later on
    Category = models.ForeignKey(Category,on_delete=models.CASCADE, null = True)
    Brand = models.ForeignKey(Brand,on_delete=models.CASCADE, null = True)
    Inserted_On = models.DateTimeField(null = True, auto_now=False,auto_now_add=True)
    updated_On = models.DateTimeField(auto_now=True,auto_now_add=False)
    
    def __str__(self):
        return self.Product_Name
