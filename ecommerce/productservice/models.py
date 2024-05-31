from django.db import models
from ecommerce.basemodels import TimeStampedModel 

class Product(TimeStampedModel): 
    name = models.CharField(max_length=100) 
    description = models.CharField(max_length=100) 
    price = models.CharField(max_length=100) 
    stock = models.CharField(max_length=100) 
