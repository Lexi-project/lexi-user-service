from userapp.grpc.grpc_files import user_pb2, user_pb2_grpc
from grpc_reflection.v1alpha import reflection


def grpc_hook(server):
    user_pb2_grpc.add_UserServiceServicer_to_server(
        UserServiceServicer(), server)
    SERVICE_NAMES = (
        user_pb2.DESCRIPTOR.services_by_name['UserService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)


class UserServiceServicer(user_pb2_grpc.UserServiceServicer):
    pass
