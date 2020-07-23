from rest_framework import serializers

from django.core.exceptions import ValidationError

from ..models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'