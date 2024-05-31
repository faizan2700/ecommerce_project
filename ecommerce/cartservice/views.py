from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet 
from rest_framework.pagination import PageNumberPagination 
from cartservice.models import Cart 
from cartservice.serializers import CartSerializer

class CartViewSet(ModelViewSet): 
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE'] 
    authentication_classes = []
    permission_classes = [] 
    lookup_field = 'pk' 
    pagination_class = PageNumberPagination 
    queryset = Cart.objects.all() 
    serializer_class = CartSerializer 