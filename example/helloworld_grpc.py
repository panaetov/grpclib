# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: example/helloworld.proto
# plugin: grpclib.plugin.main
from abc import ABCMeta, abstractmethod

import grpclib.const
import grpclib.client

import example.helloworld_pb2


class GreeterBase(metaclass=ABCMeta):

    @abstractmethod
    async def SayHello(self, stream):
        pass

    def __mapping__(self):
        return {
            '/helloworld.Greeter/SayHello': grpclib.const.Handler(
                self.SayHello,
                grpclib.const.Cardinality.UNARY_UNARY,
                example.helloworld_pb2.HelloRequest,
                example.helloworld_pb2.HelloReply,
            ),
        }


class GreeterStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SayHello = grpclib.client.UnaryUnaryMethod(
            channel,
            '/helloworld.Greeter/SayHello',
            example.helloworld_pb2.HelloRequest,
            example.helloworld_pb2.HelloReply,
        )
