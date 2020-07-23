from rest_framework.views import APIView

from ..models import Question
from ..serializers.QuestionSerializers import QuestionSerializer
from shared.responses import Responses as response

class QuestionController(APIView):
    def get(self, request, pk):
        try:
            question = Question.objects.get(id=pk)
            serializer = QuestionSerializer(question)

            return response.status_200(data=serializer.data)
        except:
            return response.status_404(data="Question not found.")

    def put(self, request, pk):
        try:
            question = Question.objects.get(id=pk)
            serializer = QuestionSerializer(question)

            if serializer.is_valid():
                serializer.save()
                return response.status_200(data=serializer.data)

            return response.status_400(serializer.errors)
        except:
            return response.status_404(data="Question not found.")

    def delete(self, request, pk):
        try:
            question = Question.objects.get(id=pk)
            question.delete()

            return response.status_200(data="Successfully deleted.")
        except:
            return response.status_404(data="Question not found.")


class QuestionListController(APIView):
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.status_200(data=serializer.data)

        return response.status_400(serializer.errors)