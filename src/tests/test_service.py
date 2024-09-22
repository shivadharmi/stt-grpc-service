import grpc
import unittest
from concurrent import futures
from stt_service_pb2 import SpeechToTextRequest
from stt_service_pb2_grpc import add_SpeechToTextServiceServicer_to_server, SpeechToTextServiceStub
from stt_whisper_service.stt_whisper_service import SpeechToTextServicer  # Adjust the import based on your project structure
import os


class TestSpeechToTextService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start a gRPC server for testing
        cls.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        add_SpeechToTextServiceServicer_to_server(SpeechToTextServicer(), cls.server)
        cls.server.add_insecure_port('[::]:50051')
        cls.server.start()

        # Create a gRPC channel
        cls.channel = grpc.insecure_channel('localhost:50051')
        cls.stub = SpeechToTextServiceStub(cls.channel)

    @classmethod
    def tearDownClass(cls):
        # Stop the server
        cls.server.stop(0)
        cls.channel.close()

    def test_speech_to_text(self):
        # Load test audio data from the data folder
        audio_file_path = os.path.join('data', 'test_audio.wav')  # Adjust the filename as needed
        with open(audio_file_path, 'rb') as audio_file:
            test_audio_data = audio_file.read()

        request = SpeechToTextRequest(audio_data=test_audio_data)

        # Call the gRPC method
        response = self.stub.SpeechToText(request)

        # Assert the response (modify based on expected output)
        self.assertIsNotNone(response)
        self.assertIsInstance(response.text, str)  # Check if the response text is a string
        # Add more assertions as needed


if __name__ == '__main__':
    unittest.main()