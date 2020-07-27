from rest_framework.views import APIView

from ..models import Program
from ..serializers.ProgramSerializers import ProgramSerializer
from shared.responses import Responses

class ProgramController(APIView, Responses):
    def get(self, request, pk, format=None):
        try:
            program = Program.objects.get(id=pk)
            serializer = ProgramSerializer(program)

            return self.status_200(data=serializer.data)
        except:
            return self.status_404(data="Program not found.")

    def put(self, request, pk):
        try:
            program = Program.objects.get(id=pk)
            serializer = ProgramSerializer(program, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return self.status_200(data=serializer.data)

            return self.status_400(serializer.errors)
        except:
            return self.status_404(data="Program not found.")

    def delete(self, request, pk):
        try:
            program = Program.objects.get(id=pk)
            program.delete()

            return self.status_200(data="Successfully deleted.")
        except:
            return self.status_404(data="Program not found.")


class ProgramListController(APIView, Responses):
    def post(self, request):
        serializer = ProgramSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return self.status_200(data=serializer.data)

        return self.status_400(serializer.errors)