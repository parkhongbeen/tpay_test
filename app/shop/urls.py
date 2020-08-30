from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop.views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='Product')

urlpatterns = [
    path('', include(router.urls)),
]
