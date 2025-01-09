from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

generated_transcription_test="Good morning, I'm Dr. Carter. I see this is your first visit with us, \
  so we'll start by gathering some general information before we talk about your specific concerns. \
  Can you confirm your full name and date of birth for me? Sure, I'm Alex Morgan, born July 15, 1990. \
  Great, thanks, Alex. Before we dive into your symptoms, do you have any medical conditions, allergies,\
  or are you taking any regular medications? No allergies, and I don't have any medical conditions that \
  I know of. I take a multivitamin, but that's about it. Understood. Now, let's talk about what brought \
  you in today. Can you describe what's been bothering you? Well, I've been having this pain in my ankle, \
  ostly at the back, near the heel. It started about a week ago. Hmm, I see. Is the pain constant, or does\
  it come and go? It's not constant. It's more noticeable when I walk, especially if I've been sitting \
  for a while and then get up. Does the pain worsen with any specific activity, like running or climbing\
  stairs? Yes, running makes it worse. I actually had to stop my jogging routine because of it. \
  I'm sorry to hear that. Have you noticed any swelling, stiffness, or redness in the area? Not really. \
  It's more like a sharp pain when I move a certain way, but the area looks normal to me. How about your \
  shoes? Have you changed footwear recently or started using any new insoles? Not that I can think of. \
  I've been using the same running shoes for a few months. Hmm. And before this started, did you have \
  any injury to your foot or leg, even a minor one? No, nothing like that. It just came out of nowhere,\
  really. Got it. One last thing—have you experienced similar pain before, or is this completely new? \
  This is completely new. I'm starting to get a little worried about it. I understand. Based on what\
  you've described, there are a few possibilities we'll need to rule out. Achilles tendonitis is one \
  of them. This condition can result from repetitive strain, especially if you've been increasing \
  physical activity. To confirm, I'll need to do a physical exam and might recommend imaging tests \
  if needed. Sound good? Yes, that makes sense. Thanks for explaining. Of course. We'll figure this out together."

prompt="This is a transcription of a conversation between a doctor and a patient during a medical consultation. Extract \
  and summarize the key details into concise, structured bullet points typically found in medical notes. Avoid narrative style. \
  Use this general format: Patient name: [Name] Date of birth: [DOB] Reason for visit: [Reason] Medical history: [Details] Current medications: [Details]\
  Symptoms described: [Details] Observations by the doctor: [Details] Next steps: [Plan or recommendations]\
Make sure the bullet points are as brief and specific as possible while accurately reflecting the key details from the conversation."

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": prompt},
        {
            "role": "user",
            "content": generated_transcription_test
        }
    ]
)
print("-------------------------------------------")
print(completion.choices[0].message.content)