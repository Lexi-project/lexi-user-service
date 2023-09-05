from grpc_reflection.v1alpha import reflection
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.tokens import BlacklistMixin

from userapp.grpc.grpc_files import user_pb2
from userapp.grpc.grpc_files import user_pb2_grpc
from userapp.models import User


def grpc_hook(server):
    user_pb2_grpc.add_UserServiceServicer_to_server(
        UserServiceServicer(), server)
    SERVICE_NAMES = (
        user_pb2.DESCRIPTOR.services_by_name['UserService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)


def validate_token(token: str) -> bool:
    try:
        access_token = AccessToken(token)
        BlacklistMixin.check_blacklist(access_token)
        user_id = access_token.payload.get('user_id')
        user = User.objects.get(id=user_id)
        return user is not None
    except Exception as e:
        return False


class UserServiceServicer(user_pb2_grpc.UserServiceServicer):

    def ValidateToken(self, request, context):
        is_valid = validate_token(request.token)
        return user_pb2.Validate(is_valid=is_valid)
