# Import necessary libraries
import io

from src.stt.stt_model_whisper import WhisperModel
from stt_service_pb2 import SpeechToTextRequest, SpeechToTextResponse
from stt_service_pb2_grpc import (
    SpeechToTextService,
)


class SpeechToTextWhisperServicer(SpeechToTextService):
    """
    A gRPC servicer for speech-to-text conversion using the Whisper model.
    """

    def __init__(self):
        """
        Initialize the SpeechToTextServicer with a Whisper model.
        """
        # Initialize the Whisper model
        self.whisper_model = WhisperModel()

    def SpeechToText(self, request: SpeechToTextRequest, context):
        """
        Convert speech to text using the Whisper model.

        Args:
            request (SpeechToTextRequest): The gRPC request containing audio data.
            context: The gRPC context.

        Returns:
            SpeechToTextResponse: The gRPC response containing the transcribed text.
        """
        # Extract audio data from the request
        audio_data = request.audio_data
        # Convert audio data to BinaryIO for processing
        audio_data = io.BytesIO(audio_data)
        # Transcribe the audio using the Whisper model
        text = self.whisper_model.transcribe_and_process(audio_data)
        # Create and return the response with the transcribed text
        response = SpeechToTextResponse(text=text)
        return response
