from rest_framework import serializers

from django.core.exceptions import ValidationError

from ..models import Section, Program
from ..serializers.ProgramSerializers import ProgramSerializer

class SectionRequestSerializer(serializers.ModelSerializer):
    program = serializers.PrimaryKeyRelatedField(queryset=Program.objects.all())

    class Meta:
        model = Section
        fields = '__all__'

    def validate_order_index(self, value):
        program = Program.objects.get(id=self.initial_data['program'])
        latest_section = Section.objects.filter(program_id=program.id).last()

        if value <= latest_section.order_index:
            raise ValidationError("Order Index must be unique per Program. "
                                  "Enter a number greater than {}".format(latest_section.order_index))
        return value

    def create(self, validated_data):
        return Section.objects.create(**validated_data)

class SectionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'