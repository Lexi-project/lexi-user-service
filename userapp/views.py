from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes


# Create your views here.


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def check_health(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1 from userapp_user")
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)
