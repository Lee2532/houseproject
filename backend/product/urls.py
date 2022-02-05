from django.contrib import admin
from django.urls import path

from .views import ProductList, ProductDetail

urlpatterns = [
    path("", ProductList.as_view(), name="product"),
    path("<int:pk>", ProductDetail.as_view(), name="product-detail"),

]
