"""
ai_backend.py

Backend for Curriculum Designer MVP
"""

import json
import os

from dotenv import load_dotenv
from groq import Groq

from prompt import get_prompt

# -------------------------------------------------------
# Load Environment Variables
# -------------------------------------------------------

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)

# -------------------------------------------------------
# Initialize Groq Client
# -------------------------------------------------------

client = Groq(api_key=GROQ_API_KEY)


# -------------------------------------------------------
# LLM Invocation
# -------------------------------------------------------

def generate_curriculum(
    subject: str,
    target_audience: str,
    prerequisites: str,
    duration: int,
) -> dict:
    """
    Generates a curriculum using the Groq LLM.

    Returns:
        dict: Curriculum as a Python dictionary.
    """

    prompt = get_prompt(
        subject=subject,
        target_audience=target_audience,
        prerequisites=prerequisites,
        duration=duration,
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0.3,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert curriculum designer. "
                    "Return ONLY valid JSON."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return json.loads(response.choices[0].message.content)


# -------------------------------------------------------
# Test
# -------------------------------------------------------

if __name__ == "__main__":

    curriculum = generate_curriculum(
        subject="AI Mastery",
        target_audience="Third Year Computer Science Engineering Students",
        prerequisites="Python, Data Structures, DBMS, Operating Systems",
        duration=200,
    )

    print(json.dumps(curriculum, indent=4))