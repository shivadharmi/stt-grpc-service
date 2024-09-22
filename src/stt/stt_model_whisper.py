import torchaudio
import torch
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
import logging
from .stt_model import STTModel

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

class WhisperModel(STTModel):
    """
    Implementation of the Whisper STT model.
    """

    def __init__(self) -> None:
        """
        Initialize the WhisperModel and load the model.
        """
        self.processor: AutoProcessor
        self.model: AutoModelForSpeechSeq2Seq
        self.load_model()

    def load_model(self) -> None:
        """
        Load the Whisper model and processor.
        """
        logging.info("Loading Whisper model and processor")
        self.processor = AutoProcessor.from_pretrained("openai/whisper-large-v3")
        self.model = AutoModelForSpeechSeq2Seq.from_pretrained(
            "openai/whisper-large-v3"
        )
        logging.info("Whisper model and processor loaded successfully")

    def preprocess_audio(
        self, audio_tensor: torch.Tensor, sample_rate: int
    ) -> torch.Tensor:
        """
        Preprocess the audio input for the Whisper model.

        Args:
            audio_tensor (torch.Tensor): The input audio tensor.
            sample_rate (int): The sample rate of the input audio.

        Returns:
            torch.Tensor: The preprocessed input features.
        """
        if sample_rate != 16000:
            logging.info(f"Resampling audio from {sample_rate}Hz to 16000Hz")
            resampler = torchaudio.transforms.Resample(
                orig_freq=sample_rate, new_freq=16000
            )
            audio_tensor = resampler(audio_tensor)

        logging.info("Preprocessing audio")
        return self.processor(
            audio_tensor.squeeze(), sampling_rate=16000, return_tensors="pt"
        ).input_features

    def transcribe(self, input_features: torch.Tensor) -> str:
        """
        Transcribe the preprocessed audio features using the Whisper model.

        Args:
            input_features (torch.Tensor): The preprocessed input features.

        Returns:
            str: The transcribed text.
        """
        logging.info("Generating transcription")
        predicted_ids = self.model.generate(input_features)

        logging.info("Decoding transcription")
        return self.processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
