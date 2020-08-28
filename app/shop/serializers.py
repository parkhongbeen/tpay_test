from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from shop.models import Product, ProductOption, Tag


class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = (
            'pk',
            'option',
            'price',
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'pk',
            'name',
        )


class ProductSerializer(WritableNestedModelSerializer):
    # Reverse FK relation
    option = ProductOptionSerializer(many=True)
    # Direct FK relation
    tag = TagSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'pk',
            'name',
            'tag',
            'option'
        )
