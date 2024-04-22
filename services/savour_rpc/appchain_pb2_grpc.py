# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from services.savour_rpc import appchain_pb2 as appchain__pb2


class AppChainServiceStub(object):
    """scripts
    protoc --go_out=./protobuf/pb --go_opt=paths=source_relative --go-grpc_out=./protobuf/pb --go-grpc_opt=paths=source_relative appchain.proto

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.L1StakerRewardsAmount = channel.unary_unary(
                '/acorus.rpc.appchain.AppChainService/L1StakerRewardsAmount',
                request_serializer=appchain__pb2.L1StakerRewardsAmountRequest.SerializeToString,
                response_deserializer=appchain__pb2.L1StakerRewardsAmountResponse.FromString,
                )
        self.L2StakerRewardsAmount = channel.unary_unary(
                '/acorus.rpc.appchain.AppChainService/L2StakerRewardsAmount',
                request_serializer=appchain__pb2.L2StakerRewardsAmountRequest.SerializeToString,
                response_deserializer=appchain__pb2.L2StakerRewardsAmountResponse.FromString,
                )
        self.L2UnStakeRecord = channel.unary_unary(
                '/acorus.rpc.appchain.AppChainService/L2UnStakeRecord',
                request_serializer=appchain__pb2.L2UnStakeRecordRequest.SerializeToString,
                response_deserializer=appchain__pb2.L2UnStakeRecordResponse.FromString,
                )
        self.L2StakeRecord = channel.unary_unary(
                '/acorus.rpc.appchain.AppChainService/L2StakeRecord',
                request_serializer=appchain__pb2.L2StakeRecordRequest.SerializeToString,
                response_deserializer=appchain__pb2.L2StakeRecordResponse.FromString,
                )
        self.L2WithdrawRecord = channel.unary_unary(
                '/acorus.rpc.appchain.AppChainService/L2WithdrawRecord',
                request_serializer=appchain__pb2.L2WithdrawRecordRequest.SerializeToString,
                response_deserializer=appchain__pb2.L2WithdrawRecordResponse.FromString,
                )


class AppChainServiceServicer(object):
    """scripts
    protoc --go_out=./protobuf/pb --go_opt=paths=source_relative --go-grpc_out=./protobuf/pb --go-grpc_opt=paths=source_relative appchain.proto

    """

    def L1StakerRewardsAmount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def L2StakerRewardsAmount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def L2UnStakeRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def L2StakeRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def L2WithdrawRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AppChainServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'L1StakerRewardsAmount': grpc.unary_unary_rpc_method_handler(
                    servicer.L1StakerRewardsAmount,
                    request_deserializer=appchain__pb2.L1StakerRewardsAmountRequest.FromString,
                    response_serializer=appchain__pb2.L1StakerRewardsAmountResponse.SerializeToString,
            ),
            'L2StakerRewardsAmount': grpc.unary_unary_rpc_method_handler(
                    servicer.L2StakerRewardsAmount,
                    request_deserializer=appchain__pb2.L2StakerRewardsAmountRequest.FromString,
                    response_serializer=appchain__pb2.L2StakerRewardsAmountResponse.SerializeToString,
            ),
            'L2UnStakeRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.L2UnStakeRecord,
                    request_deserializer=appchain__pb2.L2UnStakeRecordRequest.FromString,
                    response_serializer=appchain__pb2.L2UnStakeRecordResponse.SerializeToString,
            ),
            'L2StakeRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.L2StakeRecord,
                    request_deserializer=appchain__pb2.L2StakeRecordRequest.FromString,
                    response_serializer=appchain__pb2.L2StakeRecordResponse.SerializeToString,
            ),
            'L2WithdrawRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.L2WithdrawRecord,
                    request_deserializer=appchain__pb2.L2WithdrawRecordRequest.FromString,
                    response_serializer=appchain__pb2.L2WithdrawRecordResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'acorus.rpc.appchain.AppChainService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AppChainService(object):
    """scripts
    protoc --go_out=./protobuf/pb --go_opt=paths=source_relative --go-grpc_out=./protobuf/pb --go-grpc_opt=paths=source_relative appchain.proto

    """

    @staticmethod
    def L1StakerRewardsAmount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/acorus.rpc.appchain.AppChainService/L1StakerRewardsAmount',
            appchain__pb2.L1StakerRewardsAmountRequest.SerializeToString,
            appchain__pb2.L1StakerRewardsAmountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def L2StakerRewardsAmount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/acorus.rpc.appchain.AppChainService/L2StakerRewardsAmount',
            appchain__pb2.L2StakerRewardsAmountRequest.SerializeToString,
            appchain__pb2.L2StakerRewardsAmountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def L2UnStakeRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/acorus.rpc.appchain.AppChainService/L2UnStakeRecord',
            appchain__pb2.L2UnStakeRecordRequest.SerializeToString,
            appchain__pb2.L2UnStakeRecordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def L2StakeRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/acorus.rpc.appchain.AppChainService/L2StakeRecord',
            appchain__pb2.L2StakeRecordRequest.SerializeToString,
            appchain__pb2.L2StakeRecordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def L2WithdrawRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/acorus.rpc.appchain.AppChainService/L2WithdrawRecord',
            appchain__pb2.L2WithdrawRecordRequest.SerializeToString,
            appchain__pb2.L2WithdrawRecordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
