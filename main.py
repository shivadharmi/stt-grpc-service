import os
from dotenv import load_dotenv
import grpc
from concurrent import futures
from stt_service_pb2_grpc import (
    add_SpeechToTextServiceServicer_to_server,
)
from src.stt_whisper_service.stt_whisper_service import SpeechToTextWhisperServicer

def serve():
    """
    Start the gRPC server for the speech-to-text service.
    """
    # Load environment variables
    load_dotenv()
    env = os.getenv("ENVIRONMENT", "local").lower()
    port = os.getenv("PORT", "50051")

    # Create a gRPC server with a thread pool executor
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Add the SpeechToTextWhisperServicer to the server
    add_SpeechToTextServiceServicer_to_server(SpeechToTextWhisperServicer(), server)

    if env == "local":
        # For local development, use insecure channel
        server.add_insecure_port(f"[::]:{port}")
    else:
        # For prod and dev environments, use secure channel
        private_key = os.getenv("SSL_PRIVATE_KEY_PATH")
        certificate_chain = os.getenv("SSL_CERTIFICATE_CHAIN_PATH")

        if not private_key or not certificate_chain:
            raise ValueError("SSL credentials not properly configured")

        server_credentials = grpc.ssl_server_credentials(
            [(open(private_key, "rb").read(), open(certificate_chain, "rb").read())]
        )
        server.add_secure_port(f"[::]:{port}", server_credentials)

    # Start the server
    server.start()
    print(f"Server started on port {port} in {env} environment")

    # Keep the server running until it is terminated
    server.wait_for_termination()


# Entry point of the script
if __name__ == "__main__":
    # Start the gRPC server
    serve()