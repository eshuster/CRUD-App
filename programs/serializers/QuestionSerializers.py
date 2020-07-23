from rest_framework import serializers

from django.core.exceptions import ValidationError

from ..models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'