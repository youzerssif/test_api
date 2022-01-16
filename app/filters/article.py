import django_filters
from app.models import Article, Category

class ArticleFilter(django_filters.FilterSet):
    
    title = django_filters.CharFilter(lookup_expr="icontains") 
    category = django_filters.CharFilter(lookup_expr="icontains", field_name="category__title") 
    category_id = django_filters.ModelMultipleChoiceFilter(
        field_name="category",
        to_field_name="id",
        queryset=Category.objects.all(),
    )
    class Meta:
        model = Article
        fields = []