from __future__ import print_function
import logging

import grpc
import connect_pb2
import connect_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = connect_pb2_grpc.ConnectStub(channel)
        response = stub.persent(connect_pb2.Request(name="CPU"))
    print("Client received CPU Persent: " + str(response.per))


if __name__ == '__main__':
    logging.basicConfig()
    run()
