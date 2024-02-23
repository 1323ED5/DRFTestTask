from django.db import models
from api.enums import RoleEnum, StatusEnum


class User(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=128, help_text='Пароль')
    last_login = models.DateTimeField(null=True, blank=True, help_text='Последний вход')
    email = models.CharField(max_length=254, unique=True)
    first_name = models.CharField(max_length=31, null=True, blank=True, help_text='Имя')
    last_name = models.CharField(max_length=31, null=True, blank=True, help_text='Фамилия')
    avatar = models.CharField(max_length=128, null=True, blank=True, help_text='Аватар')
    role = models.CharField(max_length=15, choices=RoleEnum.choices, help_text='Роль')

    def __str__(self):
        return f'User "{self.email}"'


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Category "{self.title}"'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'Product "{self.title}"'


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(choices=StatusEnum.choices, max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'Order #{self.id}'
