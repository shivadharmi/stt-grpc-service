import logging

import grpc

from stt_service_pb2 import SpeechToTextRequest
from stt_service_pb2_grpc import SpeechToTextServiceStub


def run():
    """
    Run the speech-to-text client.

    This function establishes a connection to the gRPC server, loads an audio file,
    sends a speech-to-text request, and logs the transcribed text.

    Raises:
        grpc.RpcError: If a gRPC-related error occurs.
        Exception: For any other unexpected errors.
    """
    logging.info("Starting the speech-to-text client")
    try:
        channel = grpc.insecure_channel("[::]:50051")
        stub = SpeechToTextServiceStub(channel)
        logging.info("Connected to the gRPC server")

        # load audio file from file
        try:
            with open("data/test_data.wav", "rb") as f:
                audio_data = f.read()
            logging.info("Audio file loaded successfully")
        except FileNotFoundError:
            logging.error("Audio file not found")
            return
        except IOError:
            logging.error("Error reading the audio file")
            return

        request = SpeechToTextRequest(audio_data=audio_data)
        logging.info("Sending speech-to-text request")
        response = stub.SpeechToText(request)
        logging.info(f"Transcribed text: {response.text}")
    except grpc.RpcError as e:
        logging.error(f"RPC error occurred: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    run()
