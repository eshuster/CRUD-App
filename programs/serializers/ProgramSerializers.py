from rest_framework import serializers

from django.core.exceptions import ValidationError

from ..models import Program, Section, Activity, Question, Answer

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'
