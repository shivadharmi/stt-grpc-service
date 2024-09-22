# Speech-to-Text Service

## Overview

Speech-to-Text service using gRPC and the Whisper model from Hugging Face's Transformers library. The service allows users to send audio data and receive transcribed text in response.

## Features

- gRPC-based communication for efficient data transfer.
- Utilizes the Whisper model for high-quality speech recognition.
- Includes a client for sending audio data and receiving transcriptions.
- Unit tests to ensure the functionality of the service.

## Requirements

- Python 3.10 or higher

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/speech-to-text-service.git
   cd speech-to-text-service
   ```

2. **Install Dependencies**
   Make sure to install the required packages as mentioned above:

   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

3. **Environment Variables**
   Create a `.env` file in the root directory and set the following variables for local environment:

   ```plaintext
   ENVIRONMENT=local
   PORT=50051
   ```

   For non-local environments (development or production), set the following variables:

   ```plaintext
   ENVIRONMENT=development  # or production
   SSL_PRIVATE_KEY_PATH=<path-to-private-key>
   SSL_CERTIFICATE_CHAIN_PATH=<path-to-certificate-chain>
   ```

4. **Run the gRPC Server**
   Start the server by running:

   ```bash
   python main.py
   ```

5. **Run the Client**
   In a separate terminal, run the client to send audio data:
   ```bash
   python src/client/client.py
   ```

## Testing

To run the unit tests, execute the following command:

```bash
python -m unittest discover -s src/tests
```

## Audio Data

Place your test audio files in the `data` directory. The client will look for `test_audio.wav` by default.

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.
