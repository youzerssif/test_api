from rest_framework import viewsets

from app.models import Tag
from app.serializers import TagSerializer
from app.filters import TagFilter


class TagViewSet(viewsets.ModelViewSet):
    
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filterset_class = TagFilter