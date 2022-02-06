from functools import partial
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Story
from .serializers import StorySerializer

class StoryList(APIView):
    def get(self, request):
        queryset = Story.objects.filter().order_by("-idx")
        serializer = StorySerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class StoryDetail(APIView):
    def get(self, request, pk):
        story = get_object_or_404(Story, idx=pk)
        serializer = StorySerializer(story)
        story.views +=1
        story.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        story = get_object_or_404(Story, idx=pk)
        serializer = StorySerializer(story, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        product = get_object_or_404(Story, idx=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
