from rest_framework.views import APIView

from ..models import Program
from ..serializers.ProgramSerializers import ProgramSerializer
from shared.responses import Responses as response

class ProgramController(APIView):
    def get(self, request, pk, format=None):
        try:
            program = Program.objects.get(id=pk)
            serializer = ProgramSerializer(program)

            return response.status_200(data=serializer.data)
        except:
            return response.status_404(data="Program not found.")

    def put(self, request, pk):
        try:
            program = Program.objects.get(id=pk)
            serializer = ProgramSerializer(program, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return response.status_200(data=serializer.data)

            return response.status_400(serializer.errors)
        except:
            return response.status_404(data="Program not found.")

    def delete(self, request, pk):
        try:
            program = Program.objects.get(id=pk)
            program.delete()

            return response.status_200(data="Successfully deleted.")
        except:
            return response.status_404(data="Program not found.")


class ProgramListController(APIView):
    def post(self, request):
        serializer = ProgramSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.status_200(data=serializer.data)

        return response.status_400(serializer.errors)