from django.shortcuts import render

from rest_framework import decorators, response, status 

@decorators.api_view(['POST']) 
def register(request): 
    return response.Response({'msg': 'Hello World'}) 

@decorators.api_view(['POST']) 
def login(request): 
    return response.Response({'msg': 'Hello World'}) 

@decorators.api_view(['GET']) 
def profile(request): 
    return response.Response({'msg': 'Hello World'}) 