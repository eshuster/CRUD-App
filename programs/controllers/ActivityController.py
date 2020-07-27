from rest_framework.views import APIView

from ..models import Activity
from ..serializers.ActivitySerializers import ActivitySerializer
from shared.responses import Responses

class ActivityController(APIView, Responses):
    def get(self, request, pk, section_id=None):
        try:
            activity = Activity.objects.get(id=pk)
            serializer = ActivitySerializer(activity)

            return self.status_200(data=serializer.data)
        except:
            return self.status_404(data="Activity not found.")

    def put(self, request, pk):
        try:
            activity = Activity.objects.get(id=pk)
            serializer = ActivitySerializer(activity, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return self.status_200(data=serializer.data)

            return self.status_400(serializer.errors)
        except:
            return self.status_404(data="Activity not found.")

    def delete(self, request, pk):
        try:
            activity = Activity.objects.get(id=pk)
            activity.delete()

            return self.status_200(data="Successfully deleted.")
        except:
            return self.status_404(data="Activity not found.")

class ActivityListController(APIView, Responses):
    def get(self, request, section_id):
        try:
            activities = Activity.objects.filter(section_id=section_id)
            serializer = ActivitySerializer(activities, many=True)

            return self.status_200(data=serializer.data)
        except:
            return self.status_404(data="Activities not found.")

    def post(self, request):
        serializer = ActivitySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return self.status_200(data=serializer.data)

        return self.status_400(serializer.errors)

