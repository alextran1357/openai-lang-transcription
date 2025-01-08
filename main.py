from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

audio_file = open("sound_recordings/recording_test.mp3", "rb")
transcript = client.audio.transcriptions.create(
  prompt="You are a doctor speaking",
  model="whisper-1",
  file=audio_file
)
print(transcript.text)