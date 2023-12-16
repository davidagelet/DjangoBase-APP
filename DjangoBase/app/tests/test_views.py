from django.test import TestCase, Client
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


class SearchCoordsViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name="exampleproduct", reference="example001", volume=100.0)

    def setUp(self):
        self.client = Client()

    def test_search_coords_no_product(self):
        response = self.client.get(reverse('app:search_coords'))
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'error': 'No product specified'})

    def test_search_coords_with_product(self):
        response = self.client.get(reverse('app:search_coords') + '?product=exampleproduct')
        self.assertEqual(response.status_code, 200)
        # Check if the response contains the expected product name
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'longest_product_name': 'exampleproduct'})