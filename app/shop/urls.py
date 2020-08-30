from django.conf.urls import url
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from config import settings
from shop.views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='Product')

urlpatterns = [
    path('', include(router.urls)),
]
