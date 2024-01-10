from grpc_reflection.v1alpha import reflection

from credits.grpc.grpc_files import credit_pb2, credit_pb2_grpc
from credits.grpc.servicers import CreditServiceServicer
from userapp.grpc.grpc_files import user_pb2, user_pb2_grpc
from userapp.grpc.servicers import UserServiceServicer


def grpc_hook(server):
    credit_pb2_grpc.add_CreditServiceServicer_to_server(
        CreditServiceServicer(), server)
    user_pb2_grpc.add_UserServiceServicer_to_server(
        UserServiceServicer(), server)
    SERVICE_NAMES = ['user.UserService', 'credit.CreditService']
    reflection.enable_server_reflection(SERVICE_NAMES, server)
