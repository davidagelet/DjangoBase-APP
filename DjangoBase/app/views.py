from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .word_finder import WordFinder

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def search_coords(request):
    query_product = request.GET.get('product', '')
    if not query_product:
        return JsonResponse({'error': 'No product specified'}, status=400)

    product_names = list(Product.objects.values_list('name', flat=True))

    # For the exercise I append this words from file to solve the last question
    with open('app/files/google-10000-english.txt', 'r') as file:
        words_fron_google_file = [line.strip().lower() for line in file]
    product_names += words_fron_google_file

    finder = WordFinder(product_names)
    longest_product_name = finder.longest_word(query_product)

    return JsonResponse({'longest_product_name': longest_product_name})