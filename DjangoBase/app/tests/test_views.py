from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from app.models import Product

class ProductViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(reference='12345', name='Test Product', volume=100.50)
        self.url = reverse('app:product-list') 

    def test_get_all_products(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        payload = {
            'reference': '67890',
            'name': 'Another Product',
            'volume': 200.00
        }
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

