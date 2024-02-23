from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.models import User, Category, Product, Order
from api.serializers import (
    UserSerializer,
    CategorySerializer,
    ProductSerializer,
    OrderSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['role']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_at', 'category_id', 'price', 'in_stock']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
