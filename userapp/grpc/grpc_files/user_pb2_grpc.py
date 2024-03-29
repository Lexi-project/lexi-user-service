# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import user_pb2 as user__pb2


class UserServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ValidateToken = channel.unary_unary(
            '/user.UserService/ValidateToken',
            request_serializer=user__pb2.TokenPayload.SerializeToString,
            response_deserializer=user__pb2.Validate.FromString,
        )


class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ValidateToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'ValidateToken': grpc.unary_unary_rpc_method_handler(
            servicer.ValidateToken,
            request_deserializer=user__pb2.TokenPayload.FromString,
            response_serializer=user__pb2.Validate.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'user.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class UserService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ValidateToken(request,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.UserService/ValidateToken',
                                             user__pb2.TokenPayload.SerializeToString,
                                             user__pb2.Validate.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
