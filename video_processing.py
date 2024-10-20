import os
import subprocess
import requests
import json
import base64

# Define your directories
download_dir = './downloads_dir'
audio_dir = './audio_dir'
os.makedirs(download_dir, exist_ok=True)
os.makedirs(audio_dir, exist_ok=True)

# Function to download video
def download_video(video_url):
    from pytubefix import YouTube
    try:
        yt = YouTube(video_url)
        mp4_streams = yt.streams.filter(file_extension='mp4').all()
        if not mp4_streams:
            raise Exception("No MP4 streams found.")
        d_video = mp4_streams[-1]
        d_video.download(output_path=download_dir)
        print('Video downloaded successfully!')
        return os.path.join(download_dir, d_video.default_filename)
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None

# Function to extract audio
def extract_audio(video_file_path):
    audio_file_path = os.path.join(audio_dir, 'audio.wav')
    try:
        command = [
            'ffmpeg',
            '-i', video_file_path,
            '-vn',
            '-acodec', 'pcm_s16le',
            '-ar', '44100',
            '-ac', '2',
            audio_file_path
        ]
        subprocess.run(command, check=True)
        print('Audio extracted successfully!')
        return audio_file_path
    except Exception as e:
        print(f"Audio extraction error: {e}")
        return None

# Function to transcribe audio
def transcribe_audio(audio_path, deepgram_api_key):
    deepgram_url = 'https://api.deepgram.com/v1/listen'
    with open(audio_path, 'rb') as audio_file:
        headers = {
            'Authorization': f'Token {deepgram_api_key}',
            'Content-Type': 'audio/wav'
        }
        response = requests.post(deepgram_url, headers=headers, data=audio_file)
        if response.status_code == 200:
            transcript = response.json().get('channel', {}).get('alternatives', [{}])[0].get('transcript', None)
            return transcript
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

# Function to generate audio from text
def generate_audio(text, elevenlabs_api_key, voice_id):
    eleven_labs_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/with-timestamps"
    headers = {
        "Content-Type": "application/json",
        "xi-api-key": elevenlabs_api_key
    }
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }
    response = requests.post(eleven_labs_url, json=data, headers=headers)
    if response.status_code == 200:
        audio_bytes = base64.b64decode(response.json().get("audio_base64", ""))
        with open('output.mp3', 'wb') as f:
            f.write(audio_bytes)
        print("Audio generated and saved as 'output.mp3'.")
    else:
        print(f"Error encountered during audio generation: {response.status_code}, "
              f"content: {response.text}")

# Main execution flow
if __name__ == "__main__":
    video_url = "https://youtu.be/CIpqjG4M3c0"
    deepgram_api_key = 'YOUR_DEEPGRAM_API_KEY'
    elevenlabs_api_key = 'YOUR_ELEVENLABS_API_KEY'
    voice_id = 'YOUR_VOICE_ID'

    video_file = download_video(video_url)
    if video_file:
        audio_file = extract_audio(video_file)
        if audio_file:
            transcript = transcribe_audio(audio_file, deepgram_api_key)
            if transcript:
                generate_audio(transcript, elevenlabs_api_key, voice_id)
