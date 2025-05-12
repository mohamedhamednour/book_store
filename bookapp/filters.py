from django_filters import rest_framework as filters
from .models import Review

class ReviewFilter(filters.FilterSet):
    book = filters.NumberFilter(field_name='book__id')

    class Meta:
        model = Review
        fields = ['book']