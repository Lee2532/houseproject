from functools import partial
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import User
from .serializers import UserSerializer
from houseproject.common import get_token, check_token

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
        
        if not User.objects.filter(username=username, password=password).exists():
            return Response({'message':f'아아디 또는 비밀번호가 틀렸습니다.'}, status=400) 
        payload = {
            "username" : username,
        }
        token = get_token(payload)
        data = {
            "result": {
                "access_token" : token
            }
        }
        return Response(data=data, status=status.HTTP_200_OK)
        
    def get(self, request):
        '''
        token 인증
        '''
        access_token = request.headers.get('Authorization', None)
        
        data = check_token(access_token)
        # if data == "TOKEN_EXPIRED":
        #     return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data=data, status=status.HTTP_200_OK)