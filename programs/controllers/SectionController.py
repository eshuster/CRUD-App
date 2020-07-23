from rest_framework.views import APIView

from ..models import Section
from ..serializers import SectionSerializers

from shared.responses import Responses as response

class SectionController(APIView):
    def get(self, request, pk):
        try:
            activity = Section.objects.get(id=pk)

            return response.status_200(data=activity)
        except:
            return response.status_404(data="Section not found.")

    def put(self, request, pk):
        try:
            activity = Section.objects.get(id=pk)

            return response.status_200(data=activity)
        except:
            return response.status_404(data="Section not found.")

    def delete(self, request, pk):
        try:
            activity = Section.objects.get(id=pk)

            return response.status_200(data=activity)
        except:
            return response.status_404(data="Section not found.")


class SectionListController(APIView):
    def post(self, request):
        pass