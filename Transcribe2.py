import whisper_timestamped as whisper

# Load the audio from the video
audio = whisper.load_audio(f"video.mp4")

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe the audio with timestamps
result = model.transcribe(audio, start=60, end=120)  # Transcribe from 1:00 to 2:00

# Print the transcription
print(result["text"])