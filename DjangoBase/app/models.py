from django.db import models

class Product(models.Model):
    reference = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
