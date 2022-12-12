from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListAPIView.as_view()),
    path('products/<pk>', views.ProductRetrieveAPIView.as_view()),
]
