from functools import partial
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Story, StoryComment
from .serializers import StorySerializer, StoryCommentSerializer

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

class StoryCommentList(APIView):
    '''
    댓글 작성, Paginator 기능 추가
    '''
    def get(self, request, pk):
        comment = get_list_or_404(StoryComment, story_idx=pk)
        paginator = Paginator(comment , 5) # 보여주는 갯수
        page_obj = paginator.get_page('1') #페이지는 임시 하드코딩
        serializer = StoryCommentSerializer(page_obj, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, pk):
        request.data['story_idx'] = pk
        serializer = StoryCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
