from rest_framework.views import APIView

from ..models import ContentItem
from ..serializers.ContentSerializers import ContentItemSerializer
from shared.responses import Responses

class ContentItemController(APIView, Responses):
    def get(self, request, activity_id, pk):
        try:
            content_header = ContentItem.objects.get(id=pk, content__activity_id=activity_id)
            serializer = ContentItemSerializer(content_header)

            return self.status_200(data=serializer.data)
        except:
            return self.status_404(data="ContentItem not found.")

    def put(self, request, activity_id, pk):
        try:
            content_header = ContentItem.objects.get(id=pk, content__activity_id=activity_id)
            serializer = ContentItemSerializer(content_header, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return self.status_200(data=serializer.data)

            return self.status_400(serializer.errors)
        except:
            return self.status_404(data="ContentHeader not found.")

    def delete(self, request, activity_id, pk):
        try:
            content_header = ContentItem.objects.get(id=pk, content__activity_id=activity_id)
            content_header.delete()

            return self.status_200(data="Successfully deleted.")
        except:
            return self.status_404(data="ContentItem not found.")

class ContentItemListController(APIView, Responses):
    def post(self, request):
        serializer = ContentItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return self.status_200(data=serializer.data)
        return self.status_400(serializer.errors)