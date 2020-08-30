from django.db import models


class Product(models.Model):
    name = models.CharField('상품명', max_length=100)
    tag_set = models.ManyToManyField('Tag', max_length=100, blank=True)

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    name = models.CharField('옵션명', max_length=100)
    price = models.PositiveIntegerField('가격')
    product = models.ForeignKey(Product, verbose_name='상품',
                                on_delete=models.CASCADE,
                                related_name='option_set')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('태그명', max_length=100)

    def __str__(self):
        return self.name
