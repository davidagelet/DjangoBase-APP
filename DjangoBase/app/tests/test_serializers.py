from django.test import TestCase
from app.models import Product
from app.serializers import ProductSerializer

class ProductSerializerTest(TestCase):
    def setUp(self):
        self.product_attributes = {
            'reference': '12345',
            'name': 'Test Product',
            'volume': 100.50
        }

        self.product = Product.objects.create(**self.product_attributes)
        self.serializer = ProductSerializer(instance=self.product)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'reference', 'name', 'volume', 'created'])

    def test_reference_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['reference'], self.product_attributes['reference'])
