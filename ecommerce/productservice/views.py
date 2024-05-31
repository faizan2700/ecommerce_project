from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from rest_framework.pagination import PageNumberPagination 

from productservice.models import Product 
from productservice.serializers import ProductSerializer

# Create your views here.
class ProductViewSet(ModelViewSet): 
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE'] 
    authentication_classes = [] 
    lookup_field = 'pk' 
    pagination_class = PageNumberPagination 
    permission_classes = [] 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer