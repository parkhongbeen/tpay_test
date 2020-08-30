from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.response import Response

from shop.models import Product
from shop.serializers import ProductSerializer


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary='Product List',
    operation_description='Product의 List를 보여줍니다.'
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_summary='Product create',
    operation_description='Product의 Create를 보여줍니다.',
))
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        temp = self.get_object(pk)
        serializer = ProductSerializer(temp, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
