from django.db import models

from ecommerce.basemodels import TimeStampedModel 
from authenticationservice.models import User 
from productservice.models import Product 

class Cart(TimeStampedModel): 
    user = models.ForeignKey(User, related_name='carts', related_query_name='carts') 

    def __str__(self): 
        return f'<Cart: {self.id}>' 

class CartItemTable(TimeStampedModel): 
    cart = models.ForeignKey(Cart, related_name='cart_items', related_query_name='cart_items') 
    product = models.ForeignKey(Product) 
    quantity = models.IntegerField() 
    price = models.IntegerField() 

    def __str__(self): 
        return f'<Cart Item: {self.id}>'

    