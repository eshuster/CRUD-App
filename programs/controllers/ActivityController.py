from rest_framework.views import APIView

from ..models import Activity
from ..serializers.ActivitySerializers import ActivitySerializer
from shared.responses import Responses as response

class ActivityController(APIView):
    def get(self, request, pk):
        try:
            activity = Activity.objects.get(id=pk)
            serializer = ActivitySerializer(activity)

            return response.status_200(data=serializer.data)
        except:
            return response.status_404(data="Activity not found.")

    def put(self, request, pk):
        try:
            activity = Activity.objects.get(id=pk)
            serializer = ActivitySerializer(activity, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return response.status_200(data=serializer.data)

            return response.status_400(serializer.errors)
        except:
            return response.status_404(data="Activity not found.")

    def delete(self, request, pk):
        try:
            activity = Activity.objects.get(id=pk)
            activity.delete()

            return response.status_200(data="Successfully deleted.")
        except:
            return response.status_404(data="Activity not found.")

class ActivityListController(APIView):
    def post(self, request):
        serializer = ActivitySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.status_200(data=serializer.data)

        return response.status_400(serializer.errors)

