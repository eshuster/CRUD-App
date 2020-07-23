from rest_framework import serializers

from django.core.exceptions import ValidationError

from ..models import ContentHeader, ContentItem

class ContentHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentHeader
        fields = '__all__'

class ContentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentItem
        fields = '__all__'