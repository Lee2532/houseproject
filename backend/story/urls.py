from django.contrib import admin
from django.urls import path
from .views import StoryList

urlpatterns = [
    path("", StoryList.as_view(), name="stroy"),

]
