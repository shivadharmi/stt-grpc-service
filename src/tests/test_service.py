import unittest
from concurrent import futures

import grpc

from src.stt_whisper_service.stt_whisper_service import (
    SpeechToTextWhisperServicer,  # Adjust the import based on your project structure
)
from stt_service_pb2 import SpeechToTextRequest
from stt_service_pb2_grpc import (
    SpeechToTextServiceStub,
    add_SpeechToTextServiceServicer_to_server,
)


class TestSpeechToTextService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start a gRPC server for testing
        cls.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        add_SpeechToTextServiceServicer_to_server(
            SpeechToTextWhisperServicer(), cls.server
        )
        cls.server.add_insecure_port("[::]:50051")
        cls.server.start()

        # Create a gRPC channel
        cls.channel = grpc.insecure_channel("localhost:50051")
        cls.stub = SpeechToTextServiceStub(cls.channel)

    @classmethod
    def tearDownClass(cls):
        # Stop the server
        cls.server.stop(0)
        cls.channel.close()

    def test_speech_to_text(self):
        # Load test audio data from the data folder
        with open("data/test_data.wav", "rb") as f:
            audio_data = f.read()

        request = SpeechToTextRequest(audio_data=audio_data)

        # Call the gRPC method
        response = self.stub.SpeechToText(request)

        # Assert the response (modify based on expected output)
        self.assertIsNotNone(response)
        self.assertIsInstance(
            response.text, str
        )  # Check if the response text is a string
        # Add more assertions as needed


if __name__ == "__main__":
    unittest.main()
