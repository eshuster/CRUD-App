from rest_framework import serializers

from django.core.exceptions import ValidationError

from ..models import Program, Section, Activity, Question, Answer

class ProgramRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

    def validate(self, data):
        return data

class ProgramResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class SectionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

    def validate_order_index(self, value):
        program = Program.objects.get(id=self.program)
        latest_section = Section.objects.latest(program_id=program.id)

        if value <= latest_section.order_index:
            raise ValidationError("Order Index must be ubnique per Program")
        return value

    def validate(self, data):
        return data

class SectionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'