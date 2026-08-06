"""
AI Data Analysis Assistant

Requirements

pip install groq
pip install pandas
"""

import pandas as pd
from groq import Groq

# --------------------------------------------------
# Load API Key
# --------------------------------------------------

KEY_PATH = r"samsung-ai\key-vault\groq-api.key"

with open(KEY_PATH) as f:
    api_key = f.read().strip()

client = Groq(api_key=api_key)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

csv_file = input("Enter CSV file path: ")

df = pd.read_csv(csv_file)

print("\nDataset Loaded Successfully")
print(f"Rows    : {len(df)}")
print(f"Columns : {len(df.columns)}")

print("\nColumns")

for c in df.columns:
    print("-", c)

# --------------------------------------------------
# Interactive Loop
# --------------------------------------------------

while True:

    question = input("\nAsk a question (exit to quit): ")

    if question.lower() in ["exit", "quit", "stop"]:
        break

    prompt = f"""
You are an expert Python data analyst.

A pandas dataframe called df is already loaded.

Columns

{list(df.columns)}

Data Types

{df.dtypes}

Generate ONLY executable Python Pandas code.

Rules

1. Return ONLY Python code.
2. No markdown.
3. No explanation.
4. Store final output in variable result.
5. Use dataframe df.

Question

{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
    )

    code = response.choices[0].message.content.strip()

    print("\nGenerated Code\n")
    print(code)

    local_vars = {"df": df}

    try:

        exec(code, {}, local_vars)

        print("\nResult\n")

        print(local_vars["result"])

    except Exception as e:

        print("\nExecution Error")

        print(e)