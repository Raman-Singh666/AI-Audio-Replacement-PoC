import streamlit as st
import whisper
import requests
import time
import os
from dotenv import load_dotenv

# Streamlit UI
st.title("AI Audio Replacement PoC")
uploaded_file = st.file_uploader("Upload a Video", type=["mp4", "avi", "mov", "mpeg"])

# Hugging Face API key
load_dotenv()  # Load environment variables from .env file
hugging_face_api_key = os.getenv("HUGGING_FACE_API_KEY")  # Replace with your actual Hugging Face API key

# Function to transcribe audio from video
def transcribe_audio(video_path):
    model = whisper.load_model("base", device="cpu")  # Whisper model for transcription
    result = model.transcribe(video_path)
    return result["text"]

# Function to generate AI voice using a known working TTS model
def generate_ai_voice(text, retries=3, wait_time=20):
    api_url = "https://api-inference.huggingface.co/models/facebook/fastspeech2-en-ljspeech"  
    headers = {
        "Authorization": f"Bearer {hugging_face_api_key}"
    }

    payload = {
        "inputs": text,  
    }

    # Create the output directory if it doesn't exist
    output_dir = './output'
    os.makedirs(output_dir, exist_ok=True)

    for attempt in range(retries):
        # st.write(f"Attempt {attempt + 1} of {retries}...")
        # st.write(f"Payload: {payload}")  # Print the payload for debugging

        response = requests.post(api_url, headers=headers, json=payload)
        st.write(f"Response Status Code: {response.status_code}")

        if response.status_code == 200:
            if response.headers.get('Content-Type').startswith('audio/'):
                audio_file_path = os.path.join(output_dir, 'output_audio.wav')  # Save to output directory
                with open(audio_file_path, 'wb') as audio_file:
                    audio_file.write(response.content)
                st.success(f"AI voice audio saved as {audio_file_path}")
                return audio_file_path
        else:
            error_details = response.text
            st.error(f"Failed to generate AI voice: {response.status_code} - {error_details}")
            
            if response.status_code == 503:
                st.write(f"Model is busy, waiting for {wait_time} seconds...")
                time.sleep(wait_time)  # Wait before retrying

    st.error("Max retries reached. Please try again later.")
    return None

# Check if a file has been uploaded
if uploaded_file is not None:
    video_path = f"./media/{uploaded_file.name}"
    
    # Save the uploaded video file
    with open(video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Extract and display the transcribed audio
    st.write("Audio extracted from video:")
    transcribed_text = transcribe_audio(video_path)
    st.write(transcribed_text)
    
    # Generate AI voice
    st.write("Replacing audio with AI voice...")
    ai_voice = generate_ai_voice(transcribed_text)
    
    if ai_voice:
        st.write("AI Voice Data Received:")
        if isinstance(ai_voice, str) and ai_voice.endswith('.wav'):
            st.audio(ai_voice)  # Play the audio file if it's an audio file path
