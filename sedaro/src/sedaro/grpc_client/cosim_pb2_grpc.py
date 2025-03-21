# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import cosim_pb2 as cosim__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in cosim_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CosimStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SimulationCall = channel.unary_unary(
                '/cosim.Cosim/SimulationCall',
                request_serializer=cosim__pb2.SimulationAction.SerializeToString,
                response_deserializer=cosim__pb2.SimulationResponse.FromString,
                _registered_method=True)
        self.AuthorizeCall = channel.unary_unary(
                '/cosim.Cosim/AuthorizeCall',
                request_serializer=cosim__pb2.Authorize.SerializeToString,
                response_deserializer=cosim__pb2.AuthorizeResponse.FromString,
                _registered_method=True)


class CosimServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SimulationCall(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuthorizeCall(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CosimServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SimulationCall': grpc.unary_unary_rpc_method_handler(
                    servicer.SimulationCall,
                    request_deserializer=cosim__pb2.SimulationAction.FromString,
                    response_serializer=cosim__pb2.SimulationResponse.SerializeToString,
            ),
            'AuthorizeCall': grpc.unary_unary_rpc_method_handler(
                    servicer.AuthorizeCall,
                    request_deserializer=cosim__pb2.Authorize.FromString,
                    response_serializer=cosim__pb2.AuthorizeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cosim.Cosim', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cosim.Cosim', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Cosim(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SimulationCall(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cosim.Cosim/SimulationCall',
            cosim__pb2.SimulationAction.SerializeToString,
            cosim__pb2.SimulationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AuthorizeCall(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cosim.Cosim/AuthorizeCall',
            cosim__pb2.Authorize.SerializeToString,
            cosim__pb2.AuthorizeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
