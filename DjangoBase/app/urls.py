from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, search_coords

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('valerdat/', include(router.urls)),
    path('valerdat/searchcoords/', search_coords, name='search_coords'),
]
