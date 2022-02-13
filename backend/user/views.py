from functools import partial
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import User
from .serializers import UserSerializer


class SignUp(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class SignIn(APIView):
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        
        if username is None or password is None:
            return Response({'message':'username 또는 password가 빠졌습니다.'}, status=400)
        
        if not User.objects.filter(username=username).exists():
            return Response({'message':f'{username} 계정이 없습니다.'}, status=400) 
        
        user = authenticate(username=username, password=password)
        
        return user
        
        
        