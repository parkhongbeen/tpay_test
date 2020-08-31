from django.test import TestCase


class ShopTest(TestCase):
    def test_product_list(self):
        response = self.client.get('/product/')
