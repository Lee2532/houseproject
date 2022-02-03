from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductList(APIView):
    
    def get(self, request):
        queryset = Product.objects.filter().order_by("-idx")
        serializer = ProductSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetail(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(idx=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        serializer = ProductSerializer(product)
        
        return Response(serializer.data, status=status.HTTP_200_OK)