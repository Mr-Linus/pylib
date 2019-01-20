import time
import logging
from concurrent import futures

import grpc

import connect_pb2
import connect_pb2_grpc

import lib.system.core as core

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Connect(connect_pb2_grpc.ConnectServicer):

    def persent(self, request, context):
        return connect_pb2.ReplyInt(per=core.SYSTEM().CPU().get_percent())


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    connect_pb2_grpc.add_ConnectServicer_to_server(Connect(), server)
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
