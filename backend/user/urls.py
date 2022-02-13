from django.contrib import admin
from django.urls import path
from .views import SignIn, SignUp

urlpatterns = [
    path("", SignIn.as_view(), name="sign-ip"),
    path("sign-up", SignUp.as_view(), name="sign-up")
]
