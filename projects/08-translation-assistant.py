"""
AI Text Translation & Summarization Assistant

Requirements

pip install groq
"""

from groq import Groq

# --------------------------------------------------
# Load API Key
# --------------------------------------------------

KEY_PATH = r"samsung-ai\key-vault\groq-api.key"

with open(KEY_PATH) as f:
    api_key = f.read().strip()

client = Groq(api_key=api_key)

# --------------------------------------------------
# Read Multi-line Input
# --------------------------------------------------

def read_text():

    print("\nEnter/Paste your text.")
    print("Press ENTER twice to finish.\n")

    lines = []

    while True:

        line = input()

        if line == "":
            break

        lines.append(line)

    return "\n".join(lines)

# --------------------------------------------------
# Main Menu
# --------------------------------------------------

print("=" * 60)
print("AI TEXT TRANSLATION & SUMMARIZATION ASSISTANT")
print("=" * 60)

print("\nChoose Operation")

print("1. Translate")
print("2. Summarize")

choice = input("\nChoice: ")

# --------------------------------------------------
# Translation
# --------------------------------------------------

if choice == "1":

    language = input("\nTarget Language: ")

    text = read_text()

    prompt = f"""
You are a professional translator.

Translate the following text into {language}.

Requirements:

- Preserve formatting.
- Preserve names.
- Preserve technical terms where appropriate.
- Return only the translated text.

Text:

{text}
"""

# --------------------------------------------------
# Summarization
# --------------------------------------------------

elif choice == "2":

    text = read_text()

    prompt = f"""
You are an expert editor.

Summarize the following text.

Provide:

1. Summary
2. Five Key Points
3. Important Keywords
4. Target Audience
5. One-Sentence Summary

Write in simple English.

Text:

{text}
"""

else:

    print("Invalid Choice")
    exit()

# --------------------------------------------------
# Call Groq
# --------------------------------------------------

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

# --------------------------------------------------
# Display Output
# --------------------------------------------------

print("\n" + "=" * 70)

if choice == "1":
    print("TRANSLATION")
else:
    print("SUMMARY")

print("=" * 70)

print(response.choices[0].message.content)