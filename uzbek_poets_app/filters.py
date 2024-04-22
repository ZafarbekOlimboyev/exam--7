from django_filters import FilterSet, CharFilter, NumberFilter
from django.db.models import Q

from uzbek_poets_app.models import PoetsModel


class PoetsFilter(FilterSet):
    search = CharFilter(method='my_filter', label='Search')

    class Meta:
        model = PoetsModel
        fields = []

    def my_filter(self, queryset, name, value):
        if value:
            return queryset.filter(
                Q(poet_name__icontains=value) |
                Q(poet_description__icontains=value) |
                Q(poet_about__icontains=value) |
                Q(poet_birthdate__icontains=value) |
                Q(poet_dead_date__icontains=value))
        else:
            return queryset
