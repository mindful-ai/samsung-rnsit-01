"""
AI YouTube Video Summarizer
Author : Workshop Demo

Requirements:
pip install groq
pip install youtube-transcript-api
pip install yt-dlp
"""

import re
from groq import Groq
from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp


# ----------------------------------------------------
# Load Groq API Key
# ----------------------------------------------------

KEY_PATH = r"samsung-ai\key-vault\groq-api.key"

with open(KEY_PATH, "r") as f:
    api_key = f.read().strip()

client = Groq(api_key=api_key)


# ----------------------------------------------------
# Extract Video ID
# ----------------------------------------------------

def extract_video_id(url):

    patterns = [
        r"v=([^&]+)",
        r"youtu\.be/([^?]+)",
        r"embed/([^?]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None


# ----------------------------------------------------
# Get Video Title
# ----------------------------------------------------

def get_video_title(url):

    try:

        ydl_opts = {
            "quiet": True,
            "skip_download": True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info["title"]

    except:
        return "Unknown Title"


# ----------------------------------------------------
# Download Transcript
# ----------------------------------------------------

def get_transcript(video_id):

    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    text = " ".join([item["text"] for item in transcript])

    return text


# ----------------------------------------------------
# Summarize using Groq
# ----------------------------------------------------

def summarize(transcript):

    prompt = f"""
You are an expert technical educator.

Summarize the following YouTube transcript.

Return the result using the following sections.

Video Summary

Five Key Points

Three Important Takeaways

Important Keywords

Difficulty Level

Target Audience

Recommended Next Steps

Transcript:

{transcript}
"""

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3,
    )

    return response.choices[0].message.content


# ----------------------------------------------------
# Main Program
# ----------------------------------------------------

print("=" * 60)
print("AI YOUTUBE VIDEO SUMMARIZER")
print("=" * 60)

url = input("\nEnter YouTube URL:\n")

video_id = extract_video_id(url)

if video_id is None:
    print("\nInvalid YouTube URL")
    exit()

print("\nFetching video information...")

title = get_video_title(url)

print("Downloading transcript...")

try:

    transcript = get_transcript(video_id)

except Exception:

    print("\nTranscript unavailable for this video.")
    exit()

print("Generating summary using Groq...\n")

summary = summarize(transcript)

print("=" * 70)
print("VIDEO TITLE")
print("=" * 70)
print(title)

print()

print("=" * 70)
print("AI SUMMARY")
print("=" * 70)

print(summary)