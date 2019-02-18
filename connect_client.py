from __future__ import print_function
import logging

import grpc
import grpc_lib.connect_pb2 as connect_pb2
import grpc_lib.connect_pb2_grpc as connect_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = connect_pb2_grpc.SystemStub(channel)
        response = stub.cpu(connect_pb2.Request(name="per"))
    print("Client received CPU Persent: " + str(response.result))


if __name__ == '__main__':
    logging.basicConfig()
    run()
