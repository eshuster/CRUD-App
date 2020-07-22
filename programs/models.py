from django.db import models

class BaseInfo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Program(BaseInfo):
    class CategoryChoices(models.TextChoices):
        LEADERSHIP_DEVELOPMENT = 'Leadership Development Program'
        COGNITIVE_BEHAVIORAL_THERAPY = 'Cognitive Behavioral Therapy'
        NEW_PARENTING = 'New Parenting'
        MINDFUL_COMMUNICATION = 'Mindful Communication'

    category = models.CharField(
        max_length=50,
        choices = CategoryChoices.choices,
        default=CategoryChoices.LEADERSHIP_DEVELOPMENT
    )

class Section(BaseInfo):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, blank=True, null=True)
    order_index = models.IntegerField(blank=True, null=True) # Sections of the same program have unique order_indexes

class Activity(BaseInfo):
    class TypeChoices(models.TextChoices):
        CONTENT = 'Content'
        QUESTION_ANSWERS = 'Question/Answers'

    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(
        max_length=20,
        choices = TypeChoices.choices,
        default=TypeChoices.CONTENT
    )
    content = models.TextField(max_length=500, blank=True, null=True) # Is not None when type is TypeChoices.CONTENT

class Question(models.Model):
    text = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)




