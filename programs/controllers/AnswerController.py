from rest_framework.views import APIView

from ..models import Answer
from ..serializers.AnswerSerializers import AnswerSerializer
from shared.responses import Responses as response

class AnswerController(APIView):
    def get(self, request, pk):
        try:
            answer = Answer.objects.get(id=pk)
            serializer = AnswerSerializer(answer)

            return response.status_200(data=serializer.data)
        except:
            return response.status_404(data="Answer not found.")

    def put(self, request, pk):
        try:
            answer = Answer.objects.get(id=pk)
            serializer = AnswerSerializer(answer)

            if serializer.is_valid():
                serializer.save()
                return response.status_200(data=serializer.data)

            return response.status_400(serializer.errors)
        except:
            return response.status_404(data="Answer not found.")

    def delete(self, request, pk):
        try:
            answer = Answer.objects.get(id=pk)
            answer.delete()

            return response.status_200(data="Successfully deleted.")
        except:
            return response.status_404(data="Answer not found.")


class AnswerListController(APIView):
    def post(self, request):
        serializer = AnswerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.status_200(data=serializer.data)
        return response.status_400(serializer.errors)