"""
AI Schedule Optimizer using Groq
Workshop Solution (60 Minutes)

Requirements

pip install groq python-dotenv

Create a .env file

GROQ_API_KEY=your_api_key
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# -----------------------------------------------------
# Load API Key
# -----------------------------------------------------

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# -----------------------------------------------------
# Configuration
# -----------------------------------------------------

INPUT_FILE = "inputs/assignment.md"
OUTPUT_FILE = "outputs/solution.md"

MODEL = "llama-3.1-8b-instant"

# -----------------------------------------------------
# Read Problem Statement
# -----------------------------------------------------

try:
    problem = Path(INPUT_FILE).read_text(encoding="utf-8")
except FileNotFoundError:
    print("Input file not found.")
    exit()

# -----------------------------------------------------
# System Prompt
# -----------------------------------------------------

SYSTEM_PROMPT = """
You are an expert project scheduling assistant.

Solve the given scheduling problem.

Think carefully before answering.

Use the ReAct methodology internally.

Do not reveal your internal reasoning.

Return the answer ONLY in Markdown.

Your response must contain the following sections.

# Constraint Summary

# Dependencies

# Critical Path

# Optimized Schedule

# Objective Score

# Suggestions
"""

# -----------------------------------------------------
# Call Groq
# -----------------------------------------------------

print("Contacting Groq LLM...\n")

response = client.chat.completions.create(

    model=MODEL,

    temperature=0.2,

    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": problem
        }
    ]
)

solution = response.choices[0].message.content

# -----------------------------------------------------
# Display Result
# -----------------------------------------------------

print("=" * 70)
print(solution)
print("=" * 70)

# -----------------------------------------------------
# Save Output
# -----------------------------------------------------

Path("outputs").mkdir(exist_ok=True)

Path(OUTPUT_FILE).write_text(
    solution,
    encoding="utf-8"
)

print(f"\nSolution saved to {OUTPUT_FILE}")