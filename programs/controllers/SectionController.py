from rest_framework.views import APIView

from ..models import Program, Section
from ..serializers.ProgramSerializers import ProgramSerializer
from ..serializers.SectionSerializers import SectionRequestSerializer, SectionResponseSerializer

from shared.responses import Responses

class SectionController(APIView, Responses):
    def get(self, request, pk):
        try:
            section = Section.objects.get(id=pk)
            serializer = SectionResponseSerializer(section)

            return self.status_200(data=serializer.data)
        except:
            return self.status_404(data="Section not found.")

    def put(self, request, pk):
        try:
            section = Section.objects.get(id=pk)
            serializer = SectionRequestSerializer(section, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return self.status_200(data=serializer.data)

            return self.status_400(serializer.errors)
        except:
            return self.status_404(data="Section not found.")

    def delete(self, request, pk):
        try:
            section = Section.objects.get(id=pk)
            section.delete()

            return self.status_200(data="Successfully deleted.")
        except:
            return self.status_404(data="Section not found.")


class SectionListController(APIView, Responses):
    def post(self, request):
        section_serializer = SectionRequestSerializer(data=request.data)

        if section_serializer.is_valid():
            section_serializer.save()

            return self.status_200(data=section_serializer.data)

        return self.status_400(section_serializer.errors)