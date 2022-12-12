from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Product
from .serializers import ProductDetailSerializer


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer



class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status']
    search_fields = ['title', 'sku']