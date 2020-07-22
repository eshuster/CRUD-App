from rest_framework.response import Response
from rest_framework import status

class Responses(Response):
    # OK
    @classmethod
    def status_200(self, data=None):
        return Response(status=status.HTTP_200_OK, data=data)

    # CREATED
    @classmethod
    def status_201(self):
        return Response(status=status.HTTP_201_CREATED)

    # BAD_REQUEST
    @classmethod
    def status_400(self, data=None):
        return Response(status=status.HTTP_400_BAD_REQUEST, data=data)

    # UNAUTHORIZED
    @classmethod
    def status_401(self): # Lacks valid authenitcation credentials
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    # FORBIDDEN
    @classmethod
    def status_403(self): # Has credentials but is not allowed
        return Response(status=status.HTTP_403_FORBIDDEN)

    # NOT FOUND
    @classmethod
    def status_404(self):
        return Response(status=status.HTTP_404_NOT_FOUND)

    # INTERNAL SERVER ERROR
    @classmethod
    def status_500(self):
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # BAD_GATEWAY (Gateway receives invalid response from origin server, Domain name unresolvable)
    @classmethod
    def status_502(self):
        return Response(status=status.HTTP_502_BAD_GATEWAY)

    # SERVICE UNAVAILABLE
    @classmethod
    def status_503(self):
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)