from django.test import TestCase
from app.models import Product

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(reference='12345', name='Test Product', volume=100.50)

    def test_reference_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('reference').verbose_name
        self.assertEquals(field_label, 'reference')

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
