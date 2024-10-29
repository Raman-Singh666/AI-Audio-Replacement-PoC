# AI Audio Replacement PoC

This project demonstrates AI-based audio replacement for videos. The app allows users to upload a video, transcribe its audio using Whisper, and replace the original audio with AI-generated voice using Hugging Face's text-to-speech model.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <https://github.com/Raman-Singh666/AI-Audio-Replacement-PoC>
   cd poc-streamlit

2. Install dependencies:
	
	pip install -r requirements.txt

3. Run the Streamlit app:
	
	streamlit run app.py

## Usage

•Run app.py through Streamlit
•Open the Streamlit app in your browser.
•Upload a video file (MP4, AVI, MOV, MPEG).
•The app will transcribe the audio and replace it with AI-generated voice.


## Dependencies

•streamlit
•whisper
•requests
•torch

### Notes ###

•This app currently works best with English audio. Other languages may require different models.

## Screenshot

![image](https://github.com/user-attachments/assets/66c4b9f1-be48-4c41-bb6c-365349f77fea)


