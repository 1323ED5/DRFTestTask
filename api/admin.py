from django.contrib import admin

from api.models import User, Category, Product, Order

admin.site.register([
    User,
    Category,
    Product,
    Order
])
