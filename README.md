# AI Audio Replacement PoC

This project demonstrates AI-based audio replacement for videos. The app allows users to upload a video, transcribe its audio using Whisper, and replace the original audio with AI-generated voice using Hugging Face's text-to-speech model.

## Features
- Upload video files (MP4, AVI, MOV, MPEG).
- Transcribe audio from the uploaded video using Whisper.
- Generate AI voice from the transcribed text.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <https://github.com/Raman-Singh666/AI-Audio-Replacement-PoC>
   cd poc-streamlit

2. Install dependencies:
	
	pip install -r requirements.txt

## Usage

1. Replace the "HUGGING_FACE_API_KEY" in the app.py file with your Hugging Face API key.
2. Run the Streamlit app:
   streamlit run app.py
3. Open the Streamlit app in your browser.
4. Upload a video file (MP4, AVI, MOV, MPEG). (max size limit: 200mb)
5. The app will transcribe the audio and replace it with AI-generated voice.

## API Key

Ensure to replace "API" in the code with your actual Hugging Face API key to use the TTS model effectively.

## Environment Variables

Create a `.env` file in the project root and add your Hugging Face API key:
HUGGING_FACE_API_KEY=your_hugging_face_api_key

## Dependencies

•streamlit
•whisper
•requests
•torch

### Notes ###

•This app currently works best with English audio. Other languages may require different models.

## Screenshot

![image](https://github.com/user-attachments/assets/66c4b9f1-be48-4c41-bb6c-365349f77fea)


