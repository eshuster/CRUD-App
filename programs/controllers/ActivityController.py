from rest_framework.views import APIView
from rest_framework.response import Response

from shared.responses import Responses as response

class ActivityController(APIView):
    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass

class ActivityListController(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass