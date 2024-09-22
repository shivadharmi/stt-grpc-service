import torch
import unittest
from src.stt.stt_model_whisper import WhisperModel

class TestWhisperModel(unittest.TestCase):

    def setUp(self):
        """Set up the WhisperModel for testing."""
        self.model = WhisperModel()

    def test_preprocess_audio(self):
        """Test the audio preprocessing method."""
        audio_tensor = torch.randn(1, 16000)  # Simulated audio tensor
        sample_rate = 16000
        processed_features = self.model.preprocess_audio(audio_tensor, sample_rate)
        self.assertEqual(processed_features.shape[1], 128)  # Check output feature size

    def test_transcribe(self):
        """Test the transcription method."""
        audio_tensor = torch.randn(1, 16000)  # Simulated audio tensor
        sample_rate = 16000
        input_features = self.model.preprocess_audio(audio_tensor, sample_rate)
        transcription = self.model.transcribe(input_features)
        self.assertIsInstance(transcription, str)  # Check if output is a string

if __name__ == "__main__":
    unittest.main()