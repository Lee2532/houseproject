from rest_framework import serializers
from .models import Product, ProductReviews


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'
        
        
class ProductReviewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductReviews
        fields = '__all__'