# from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from app.views import CategoryViewSet,TagViewSet,ArticleViewSet


router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('Tag', TagViewSet, basename='Tag')
router.register('article', ArticleViewSet, basename='article')


urlpatterns = [
    # ...
]

urlpatterns += router.urls