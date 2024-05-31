from rest_framework.serializers import ModelSerializer 

from cartservice.models import Cart 

class CartSerializer(ModelSerializer): 
    class Meta: 
        fields = '__all__' 
        model = Cart 