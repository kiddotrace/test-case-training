from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from products.serializer import ProductListSerializer, ProductCreateSerializer, \
    ProductUpdateSerializer, BaseProductSerializer
from products.models import Product


class ListProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class UpdateProductAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer


class CreateProductAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class DeleteProductAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = BaseProductSerializer
