from groq import Groq

KEY_PATH = r"samsung-ai\key-vault\groq-api.key"

with open(KEY_PATH) as f:
    api_key = f.read().strip()

client = Groq(api_key=api_key)

question = input("Enter your health question:\n")

prompt = f"""
You are a qualified health educator.

Answer the following question.

Provide:

- Explanation
- Possible causes
- Healthy habits
- Prevention
- When to consult a doctor

Question:
{question}

Do not diagnose diseases.
Always include a disclaimer.
"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}],
)

print(response.choices[0].message.content)