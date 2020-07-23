from rest_framework.views import APIView

from ..models import ContentHeader, ContentItem
from ..serializers.ContentSerializers import ContentHeaderSerializer, ContentItemSerializer
from shared.responses import Responses as response

class ContentHeaderController(APIView):
    def get(self, request, pk):
        try:
            content_header = ContentHeader.objects.get(id=pk)
            serializer = ContentHeaderSerializer(content_header)

            return response.status_200(data=serializer.data)
        except:
            return response.status_404(data="ContentHeader not found.")

    def put(self, request, pk):
        try:
            content_header = ContentHeader.objects.get(id=pk)
            serializer = ContentHeaderSerializer(content_header)

            if serializer.is_valid():
                serializer.save()
                return response.status_200(data=serializer.data)

            return response.status_400(serializer.errors)
        except:
            return response.status_404(data="ContentHeader not found.")

    def delete(self, request, pk):
        try:
            content_header = ContentHeader.objects.get(id=pk)
            content_header.delete()

            return response.status_200(data="Successfully deleted.")
        except:
            return response.status_404(data="ContentHeader not found.")


class ContentHeaderListController(APIView):
    def post(self, request):
        serializer = ContentHeaderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.status_200(data=serializer.data)
        return response.status_400(serializer.errors)