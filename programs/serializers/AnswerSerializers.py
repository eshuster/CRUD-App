from rest_framework import serializers

from django.core.exceptions import ValidationError

from ..models import Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'