import django_filters
from app.models import Tag

class TagFilter(django_filters.FilterSet):
    
    name = django_filters.CharFilter(lookup_expr="icontains") 
    class Meta:
        model = Tag
        fields = []