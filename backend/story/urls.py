from django.contrib import admin
from django.urls import path
from .views import StoryList, StoryDetail,StoryCommentList

urlpatterns = [
    path("", StoryList.as_view(), name="story"),
    path("<int:pk>", StoryDetail.as_view(), name="story-detail"),
    path("<int:pk>/comment", StoryCommentList.as_view(), name="story-comment-list"),
]
