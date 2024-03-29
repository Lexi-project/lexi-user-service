from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.tokens import BlacklistMixin
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated

from userapp.models import User


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
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_authenticated_user(request: Request):
    authenticated_user = request.user
    user_id = authenticated_user.id
    return Response(
        {"user_id": user_id},
        status=status.HTTP_200_OK
    )

class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request: Request):
        access_token = request.auth.token
        token = AccessToken(access_token)
        BlacklistMixin.blacklist(token)
        return Response(status=status.HTTP_200_OK)
