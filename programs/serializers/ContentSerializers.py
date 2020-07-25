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

    def validate_order_index(self, value):
        content_header = ContentHeader.objects.get(id=self.initial_data['content_header'])
        latest_content_header = ContentItem.objects.filter(content_header_id=content_header.id).last()

        if value <= latest_content_header.order_index:
            raise ValidationError("Order Index must be unique per Program. "
                                  "Enter a number greater than {}".format(latest_content_header.order_index))
        return value
