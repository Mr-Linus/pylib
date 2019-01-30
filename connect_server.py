import time
import logging
from concurrent import futures

import grpc
import grpc_lib.connect_pb2 as connect_pb2
import grpc_lib.connect_pb2_grpc as connect_pb2_grpc
import lib.system.core as core
import lib.system.nvidia as nvdia
_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class System(connect_pb2_grpc.SystemServicer):

    def cpu(self, request, context):
        if request.name == "per":
            return connect_pb2.ReplyInt(result=core.SYSTEM().CPU().get_percent())
        elif request.name == "num":
            return connect_pb2.ReplyInt(result=core.SYSTEM().CPU().num)
        elif request.name == "Lnum":
            return connect_pb2.ReplyInt(result=core.SYSTEM().CPU().Lnum)
        else:
            return connect_pb2.ReplyInt(result=0)

    def mem(self, request, context):
        return connect_pb2.ReplyFloat(
            result=core.SYSTEM().MEM().get_mem(
                unit=request.unit,
                mtype=request.type
            )
        )
    def mem_per(self, request, context):
        return connect_pb2.ReplyInt(result=int(core.SYSTEM().MEM().get_per()))

    def swap(self, request, context):
        if request.type == 'used':
            return connect_pb2.ReplyFloat(
                result=core.SYSTEM().SWAP().used
            )
        elif request.type == 'total':
            return connect_pb2.ReplyFloat(
                result=core.SYSTEM().SWAP().total
            )
        elif request.type == 'free':
            return connect_pb2.ReplyFloat(
                result=core.SYSTEM().SWAP().free
            )
        else:
            return connect_pb2.ReplyFloat(result=0)

    def net(self, request, context):
        if request.type == 'send':
            return connect_pb2.ReplyFloat(
                result=core.SYSTEM().NET().send_MB
            )
        elif request.type == 'recv':
            return connect_pb2.ReplyFloat(
                result=core.SYSTEM().NET().recv_MB
            )
        else:
            return connect_pb2.ReplyFloat(result=0)

    def uptime(self, request, context):
        return connect_pb2.ReplyInt(result=core.SYSTEM().system_uptime())


class NVIDIA(connect_pb2_grpc.NVIDIAServicer):

    def mem(self, request, context):
        return connect_pb2.ReplyFloat(
            result=nvdia.NVIDIA().MEM().get_mem(
                unit=request.unit,
                mtype=request.type
            )
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    connect_pb2_grpc.add_SystemServicer_to_server(System(), server)
    connect_pb2_grpc.add_NVIDIAServicer_to_server(NVIDIA(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
