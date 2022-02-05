from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
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
        product = get_object_or_404(Product, idx=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        product = get_object_or_404(Product, idx=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True) #부분 업데이트 허용
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)
    