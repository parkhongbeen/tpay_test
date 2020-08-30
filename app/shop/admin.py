from django.contrib import admin

# Register your models here.
from shop.models import Tag, ProductOption, Product

admin.site.register(Product)
admin.site.register(ProductOption)
admin.site.register(Tag)
