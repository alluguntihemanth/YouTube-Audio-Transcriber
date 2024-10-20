# 🎥 **Video Processing Project**  
## 🎙️ **Deepgram & ElevenLabs Integration**  

<p align="center">
  <img src="https://cdn.prod.website-files.com/5fac161927bf86485ba43fd0/64705e36d6c173f75626cf6b_Blog-Cover-2022_02_How-to-Transcribe-Audio-to-Text-(Automatically-_-For-Free).jpeg" alt="Transcribing Audio to Text" width="400" height="220" style="margin-right: 20px;"/>
  <img src="https://www.folio3.ai/blog/wp-content/uploads/2022/03/Text-To-Speech.jpg" alt="Text to Speech" width="400"/>
</p>
 

---

## 📝 **Overview**  
This project facilitates the **download, audio extraction, transcription, and text-to-speech generation** from YouTube videos. It utilizes **Deepgram** for transcription and **ElevenLabs** for generating speech from text, streamlining the process of creating audio content from video sources.

---

## ✨ **Key Features**  
1. **Video Downloading**:  
   - Downloads YouTube videos in **MP4** format.  

2. **Audio Extraction**:  
   - Converts downloaded video files to **WAV** format for transcription.  

3. **Transcription**:  
   - Utilizes **Deepgram's API** to convert audio to text.  

4. **Text-to-Speech Generation**:  
   - Generates audio files from text using **ElevenLabs' API**, providing a smooth audio output experience.

---

## 📂 **Directory Structure**  
D:/Video-Processing-Project/
│
├── video_processing.py     # Main script for processing videos
├── downloads_dir/          # Directory where videos are downloaded
├── audio_dir/              # Directory for extracted audio files
└── requirements.txt        # List of dependencies

---

## 🚀 **Run the Application**  

1. **Prerequisites**  
   - Install [Python](https://www.python.org/downloads/).  
   - Install the necessary dependencies:  
     ```bash
     pip install pytubefix requests
     ```

2. **Set Up Your API Keys**  
   - Replace `YOUR_DEEPGRAM_API_KEY` and `YOUR_ELEVENLABS_API_KEY` in the script with your actual API keys.  
   - Specify your voice ID in the script as well.

3. **Run the Script**  
   - Execute the script to download a video, extract audio, transcribe it, and generate audio from the transcription:  
     ```bash
     python video_processing.py
     ```

---

## 💬 **Example Usage**  
To use the script, simply specify a YouTube video URL in the `video_processing.py` file. Upon execution, it will perform the following:

1. Download the video.
2. Extract audio from the video.
3. Transcribe the audio to text.
4. Generate an audio file from the transcribed text.

---

## 🛠️ **Key Functions**  
- **`download_video(video_url)`**:  
  Downloads a YouTube video and returns the file path.  
- **`extract_audio(video_file_path)`**:  
  Extracts audio from the video file and returns the audio file path.  
- **`transcribe_audio(audio_path, deepgram_api_key)`**:  
  Transcribes audio to text using Deepgram's API.  
- **`generate_audio(text, elevenlabs_api_key, voice_id)`**:  
  Generates audio from text using ElevenLabs' API.

---

## 🤝 **Contributing**  
We welcome contributions! Feel free to fork the repository and make your improvements. Guidelines for formal contributions will be established soon.

---

## 📄 **License**  
This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for more details.

---

## 📧 **Contact**  
For any inquiries, feel free to reach out via:  
- **Email**: hemanthallugunti.com  
- **LinkedIn**: [Hemanth Reddy Allugunti](https://www.linkedin.com/in/hemanth-reddy-allugunti-883b36216/)

---

Enjoy processing videos with this **Deepgram & ElevenLabs Integration** project! 🎉
