from rest_framework.views import APIView
from django.db import connections
from django.http import JsonResponse

from .models import Product
# Create your views here.
class ProductList(APIView):
    def get(self, request):
        pass