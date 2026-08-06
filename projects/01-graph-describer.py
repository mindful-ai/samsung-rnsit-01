"""
AI Graph Describer using Groq Vision API

Requirements:
pip install groq

Author: Workshop Demo
"""

import base64
from pathlib import Path
from groq import Groq


# ----------------------------------------------------
# Load Groq API Key
# ----------------------------------------------------
KEY_PATH = r"samsung-ai\key-vault\groq-api.key"

with open(KEY_PATH, "r") as f:
    api_key = f.read().strip()

client = Groq(api_key=api_key)


# ----------------------------------------------------
# Read image
# ----------------------------------------------------
image_path = input("Enter graph image path: ").strip()

if not Path(image_path).exists():
    print("Image not found.")
    exit()

with open(image_path, "rb") as img:
    image_data = base64.b64encode(img.read()).decode("utf-8")


# ----------------------------------------------------
# Prompt
# ----------------------------------------------------
prompt = """
You are an expert data analyst.

Analyze the given graph image and provide:

1. Graph Type
2. Graph Title (if available)
3. X-axis label
4. Y-axis label
5. Highest value
6. Lowest value
7. Five important observations
8. Overall summary

If any information is missing, write "Not Available".

Format the answer neatly using headings and bullet points.
"""


# ----------------------------------------------------
# Call Groq
# ----------------------------------------------------
response = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",   # Replace with your available vision model if needed
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{image_data}"
                    }
                }
            ]
        }
    ],
    temperature=0.2,
)

print("\n" + "=" * 70)
print("GRAPH DESCRIPTION")
print("=" * 70)

print(response.choices[0].message.content)