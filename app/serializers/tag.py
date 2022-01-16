from rest_framework import serializers

from app.models import Tag

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'