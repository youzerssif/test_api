from django.shortcuts import get_object_or_404
from app import serializers

from rest_framework import viewsets, permissions
from rest_framework.response import Response

from app.filters import ArticleFilter
from app.models import Article
from app.serializers import ArticleSerializer, ArticleListSerializer, CreateArticleSerializer

from core.permissions import IsOwnerOrReadOnly




class ArticleViewSet(viewsets.ModelViewSet):
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_class = ArticleFilter
    
    # permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
    
    def list(self, request):
        # queryset = Article.objects.all()
        # serializer = ArticleSerializer(queryset, many=True)
        # return Response(serializer.data)
        # self.serializer_class = ArticleListSerializer
        return super().list(request)

    # def retrieve(self, request, pk=None):
    #     queryset = Article.objects.all()
    #     article = get_object_or_404(queryset, pk=pk)
    #     serializer = ArticleSerializer(article)
    #     return Response(serializer.data)
    
    
    # def list(self, request):
    #     pass

    def create(self, request):
        serializer = CreateArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.serializer_class = CreateArticleSerializer

        return super().create(request)

        # serializer = ArticleSerializer()

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass