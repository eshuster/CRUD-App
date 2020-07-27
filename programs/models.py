from django.db import models

class BaseInfo(models.Model):
    name = models.CharField(max_length=100, unique=True)
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
    image_address = models.TextField(blank=True, null=True) # Location to image stored on S3 Bucket

class Activity(BaseInfo):
    class TypeChoices(models.TextChoices):
        CONTENT = 'HTML_Content'
        QUESTION_ANSWERS = 'Question/Answers'

    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(
        max_length=20,
        choices = TypeChoices.choices,
        default=TypeChoices.CONTENT
    )

class Content(models.Model):
    activity = models.OneToOneField(Activity, on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class ContentItem(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=50)
    order_index = models.IntegerField(blank=True, null=True) # ContentItems of the same Content have unique order_indexes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)