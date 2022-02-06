from django.contrib import admin
from django.urls import path
from .views import StoryList, StoryDetail

urlpatterns = [
    path("", StoryList.as_view(), name="story"),
    path("<int:pk>", StoryDetail.as_view(), name="story-detail"),

]
