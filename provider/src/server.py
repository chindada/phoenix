"""
provider.src.server -.
"""

import logging
import os
from concurrent import futures

import grpc
from shioaji_client import ShioajiClient

try:
    import provider_pb2_grpc
except ImportError as exc:
    raise ImportError(
        "Failed to import generated modules or ShioajiClient. "
        "Please ensure 'make codegen-py' has been run and 'provider/src' is in PYTHONPATH."
    ) from exc


class ShioajiService(provider_pb2_grpc.ShioajiProviderServicer):
    """
    ShioajiService -.
    """

    def __init__(self):
        # WARNING: This implementation is stateful and supports only a single user session.
        # It is not suitable for concurrent multi-user environments.
        self.client = ShioajiClient()
        self.logged_in = False


def serve():
    port = os.getenv("PORT", "50051")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    provider_pb2_grpc.add_ShioajiProviderServicer_to_server(ShioajiService(), server)
    server.add_insecure_port("[::]:" + port)
    logging.info("Server started, listening on %s", port)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve()
