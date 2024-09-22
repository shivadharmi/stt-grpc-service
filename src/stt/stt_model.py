import logging
from abc import ABC, abstractmethod
from typing import Any, BinaryIO

import torch
import torchaudio

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class STTModel(ABC):
    """
    Abstract base class for Speech-to-Text (STT) models.
    """

    @abstractmethod
    def load_model(self) -> None:
        """
        Load the STT model.
        """
        raise NotImplementedError("load_model() must be implemented by subclasses")

    @abstractmethod
    def preprocess_audio(self, audio_tensor: torch.Tensor, sample_rate: int) -> Any:
        """
        Preprocess the audio input.

        Args:
            audio_tensor (torch.Tensor): The input audio tensor.
            sample_rate (int): The sample rate of the input audio.

        Returns:
            Any: Preprocessed audio features.
        """
        raise NotImplementedError(
            "preprocess_audio() must be implemented by subclasses"
        )

    @abstractmethod
    def transcribe(self, input_features: Any) -> str:
        """
        Transcribe the preprocessed audio features.

        Args:
            input_features: The preprocessed audio features.

        Returns:
            str: The transcribed text.
        """
        raise NotImplementedError("transcribe() must be implemented by subclasses")

    def transcribe_and_process(self, audio: BinaryIO) -> str | None:
        """
        Process and transcribe the given audio.

        Args:
            audio (Union[str, bytes]): The input audio file path or audio data.

        Returns:
            str | None: The transcribed text or None if an error occurs.
        """
        if audio is None:
            logging.warning("Received None as audio input")
            return None

        try:
            logging.info("Loading audio file")
            audio_tensor, sample_rate = torchaudio.load(audio)

            logging.info(f"Audio loaded with sample rate: {sample_rate}")
            input_features = self.preprocess_audio(audio_tensor, sample_rate)

            logging.info("Audio preprocessed successfully")
            transcription_text = self.transcribe(input_features)

            logging.info("Transcription completed")
            return transcription_text
        except Exception as e:
            logging.error(f"An error occurred during transcription: {str(e)}")
            return None
