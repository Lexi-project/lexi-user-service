import json
from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from userapp.models import User
from userapp.serializers import UserLoginSerializer
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import AccessToken


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


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = RefreshToken.for_user(user)
        response_data = {'user_id': user.id, 'token': str(token.access_token)}
        return Response(response_data, status=status.HTTP_200_OK)
