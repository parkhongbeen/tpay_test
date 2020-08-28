from rest_framework.viewsets import ModelViewSet

from shop.models import Product
from shop.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#
# product_list = ProductViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# product_detail = ProductViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })
