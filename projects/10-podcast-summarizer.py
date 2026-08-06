"""
AI Podcast Summarizer

Requirements

pip install groq
"""

from groq import Groq

# ----------------------------------------------------
# Load API Key
# ----------------------------------------------------

KEY_PATH = r"samsung-ai\key-vault\groq-api.key"

with open(KEY_PATH) as f:
    api_key = f.read().strip()

client = Groq(api_key=api_key)

# ----------------------------------------------------
# Audio File
# ----------------------------------------------------

audio_file = input("Enter Podcast MP3 File: ")

# ----------------------------------------------------
# Speech to Text
# ----------------------------------------------------

with open(audio_file, "rb") as file:

    transcript = client.audio.transcriptions.create(

        file=file,

        model="whisper-large-v3-turbo",

        response_format="text"

    )

print("\nTranscription Completed.\n")

# ----------------------------------------------------
# Prompt
# ----------------------------------------------------

prompt = f"""
You are an expert podcast reviewer.

Analyze the following podcast transcript.

Provide

1. Summary

2. Five Key Points

3. Important Keywords

4. Main Topics

5. Action Items

6. Target Audience

7. Sentiment

8. One-line Takeaway

Transcript

{transcript}
"""

# ----------------------------------------------------
# LLM
# ----------------------------------------------------

response = client.chat.completions.create(

    model="llama-3.1-8b-instant",

    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],

    temperature=0.3

)

# ----------------------------------------------------
# Output
# ----------------------------------------------------

print("=" * 70)
print("AI PODCAST SUMMARY")
print("=" * 70)

print(response.choices[0].message.content)