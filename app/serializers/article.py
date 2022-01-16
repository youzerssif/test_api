from operator import mod
from pyexpat import model
from unicodedata import category
from rest_framework import serializers

from drf_writable_nested.serializers import WritableNestedModelSerializer

from .category import CategorySerializer

from app.models import Article, Category, Tag


class ArticleSerializer(WritableNestedModelSerializer):
    
    class EmbededCategorySerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Category
            fields = ('title','id')
            read_only_fields = ('pk',)
            
    class EmbededTagSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Tag
            fields = ('name',)
            
    category = EmbededCategorySerializer()
    tag = EmbededTagSerializer(read_only=True, many=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        
        
        
class ArticleListSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Article
        fields = ('id','title',)

class CreateArticleSerializer(serializers.ModelSerializer):
    
    # category = serializers.PrimaryKey    
    class Meta:
        model = Article
        fields = '__all__'