from rest_framework import serializers

from django.core.exceptions import ValidationError

from ..models import Content, ContentItem

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

class ContentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentItem
        fields = '__all__'

    def validate_order_index(self, value):
        # content_header = ContentHeader.objects.get(id=self.initial_data['content_header'])
        latest_content_item = ContentItem.objects.filter(content_id=self.initial_data['content']).last()

        if value <= latest_content_item.order_index:
            raise ValidationError("Order Index must be unique per Program. "
                                  "Enter a number greater than {}".format(latest_content_item.order_index))
        return value
