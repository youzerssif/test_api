from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from app.serializers.category import CategorySerializer

from app.models import Category
from app.serializers import CategorySerializer
from app.filters import CategoryFilter


class CategoryViewSet(viewsets.ModelViewSet):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter