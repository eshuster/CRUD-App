from rest_framework.views import APIView

from ..models import Content
from ..serializers.ContentSerializers import ContentSerializer
from shared.responses import Responses

class ContentController(APIView, Responses):
    def get(self, request, activity_id, pk):
        try:
            content = Content.objects.get(id=pk, activity_id=activity_id)
            serializer = ContentSerializer(content)

            return self.status_200(data=serializer.data)
        except:
            return self.status_404(data="Content not found.")

    def put(self, request, activity_id, pk):
        try:
            content = Content.objects.get(id=pk, activity_id=activity_id)
            serializer = ContentSerializer(content, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return self.status_200(data=serializer.data)

            return self.status_400(serializer.errors)
        except:
            return self.status_404(data="Content not found.")

    def delete(self, request, activity_id, pk):
        try:
            content = Content.objects.get(id=pk)
            content.delete()

            return self.status_200(data="Successfully deleted.")
        except:
            return self.status_404(data="Content not found.")


class ContentListController(APIView, Responses):
    def post(self, request):
        serializer = ContentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return self.status_200(data=serializer.data)
        return self.status_400(serializer.errors)