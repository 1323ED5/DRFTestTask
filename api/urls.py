from django.urls import path, include
from rest_framework import routers

from api.views import (
    UserViewSet,
    CategoryViewSet,
    ProductsViewSet,
    OrderViewSet
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'products', ProductsViewSet)
router.register(r'orders', OrderViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]
