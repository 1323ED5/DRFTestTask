from rest_framework import serializers

from api.models import User, Category, Product, Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ['id']
        fields = [
            'id',
            'password',
            'last_login',
            'email',
            'first_name',
            'last_name',
            'avatar',
            'role'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        read_only_fields = ['id', 'created_at', 'updated_at']
        fields = [
            'id',
            'title',
            'created_at',
            'updated_at',
            'parent_category'
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        read_only_fields = ['id', 'created_at', 'updated_at']
        fields = [
            'id',
            'title',
            'description',
            'price',
            'in_stock',
            'created_at',
            'updated_at',
            'category'
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        read_only_fields = ['id', 'created_at', 'updated_at', 'products']
        fields = [
            'id',
            'status',
            'created_at',
            'updated_at',
            'customer',
            'products'
        ]
