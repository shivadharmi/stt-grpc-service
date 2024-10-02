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
- Required packages listed in requirements.txt

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

3. **Install Pre-commit**
   To install pre-commit, run:

   ```bash
   pip install pre-commit
   ```

4. **Environment Variables**
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

5. **Run the gRPC Server**
   Start the server by running:

   ```bash
   python main.py
   ```

6. **Run the Client**
   In a separate terminal, run the client to send audio data:

   ```bash
   python src/client/client.py
   ```

7. **Run Pre-commit Hooks**
   To ensure code quality, install and run pre-commit hooks:

   ```bash
   pre-commit run --all-files
   ```

8. **Code Formatting and Linting**
   Use `ruff` for linting and `black` for code formatting:

   ```bash
   ruff check .
   black .
   ```

## Production Environment Setup

1. **Clone the Repository**
   If not already cloned, use the same command as for the development environment:

   ```bash
   git clone <https://github.com/your-username/speech-to-text-service.git>
   cd speech-to-text-service
    ```

2. **Install Dependencies**
   Install the required packages:

   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

3. **Environment Variables**
   Create a .env file in the root directory or configure your environment management tool, and set the following variables for production:

   ```bash
   ENVIRONMENT=production
   PORT=50051
   SSL_PRIVATE_KEY_PATH=<path-to-private-key>
   SSL_CERTIFICATE_CHAIN_PATH=<path-to-certificate-chain>
    ```

4. **Run the gRPC Server**
   Start the server in production mode:

   ```bash
   python main.py
   ```

## Testing

To run the unit tests, execute the following command:

```bash
python -m unittest discover -s src/tests
```

## Audio Data

Place your test audio files in the `data` directory. The client will look for `test_audio.wav` by default.

## Troubleshooting Tips

- Server Not Starting: Check that all dependencies are correctly installed and that the environment variables are set properly.
- gRPC Connection Issues: Ensure that the server is running and accessible. Verify the port and SSL configurations.
- Audio File Issues: Confirm that the audio file is in the correct format and located in the expected directory.

## Best Practices

- Regularly back up your database and any important files.
- Keep dependencies up to date to benefit from security patches and new features.
- Utilize version control effectively for collaboration.
- Monitor server performance and logs for any anomalies.
- Follow coding standards and use tools like ruff and black for code quality.

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.
