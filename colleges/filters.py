import django_filters
from .models import College

class CollegeFilter(django_filters.FilterSet):
    min_marks = django_filters.NumberFilter(field_name="cutoff_mark", lookup_expr='gte')
    max_marks = django_filters.NumberFilter(field_name="cutoff_mark", lookup_expr='lte')

    class Meta:
        model = College
        fields = ['state', 'category', 'min_marks', 'max_marks']
