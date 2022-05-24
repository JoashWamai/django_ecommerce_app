import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        models: Product
        fields: ['productName', 'category', 'brand']
