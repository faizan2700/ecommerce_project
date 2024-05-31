from rest_framwork.serializers import ModelSerializer 

from productservice.models import Product 

class ProductSerializer(ModelSerializer): 
    class Meta: 
        fields = '__all__' 
        model = Product 