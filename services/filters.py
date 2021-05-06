from services.models import Service
import django_filters


class ServicesFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Service
        fields = {'owner': ['exact', ]}
