from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

audio_file = open("sound_recordings/Recording_low_quality.mp3", "rb")
transcript = client.audio.transcriptions.create(
  prompt="You are a doctor speaking",
  model="whisper-1",
  file=audio_file
)
print("-------------------------------------------")
print("Text ", transcript.text)
# print("Transcription ", transcript)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "Summarize the provided text. Make it more concise and shorter. Provide text as if taking down quick notes"},
        {
            "role": "user",
            "content": transcript.text
        }
    ]
)
print("-------------------------------------------")
print(completion.choices[0].message.content)