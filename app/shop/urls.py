from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
