"""
AI HR Resume Screening Assistant
Workshop Version (Single File)

pip install groq python-dotenv matplotlib
"""

import os
import json
from pathlib import Path

import matplotlib.pyplot as plt
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.1-8b-instant"

# ---------------------------------------------------
# Read Job Description
# ---------------------------------------------------

job_description = Path(
    "inputs/job_description.md"
).read_text(encoding="utf-8")

# ---------------------------------------------------
# Read Candidate Profiles
# ---------------------------------------------------

profiles = []

profile_folder = Path("inputs/profiles")

for file in profile_folder.glob("*.md"):

    profiles.append({
        "name": file.stem,
        "content": file.read_text(encoding="utf-8")
    })

# ---------------------------------------------------
# Build Prompt
# ---------------------------------------------------

candidate_text = ""

for p in profiles:

    candidate_text += f"""

Candidate:
{p['name']}

Resume

{p['content']}

----------------------------------------

"""

prompt = f"""
You are an experienced HR recruiter.

Compare the following Job Description with all candidate profiles.

Job Description

{job_description}

Candidate Profiles

{candidate_text}

Return ONLY valid JSON.

Format

{{
"summary":"...",
"candidates":[
    {{
      "name":"",
      "score":95,
      "remarks":"..."
    }}
],
"top5":[
"Candidate A",
"Candidate B"
],
"recommendation":"..."
}}
"""

# ---------------------------------------------------
# Ask Groq
# ---------------------------------------------------

response = client.chat.completions.create(

    model=MODEL,

    temperature=0.2,

    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ]
)

result = json.loads(
    response.choices[0].message.content
)

# ---------------------------------------------------
# Print Results
# ---------------------------------------------------

print("\nJOB SUMMARY\n")
print(result["summary"])

print("\nCandidate Scores\n")

for c in result["candidates"]:
    print(f"{c['name']:20} {c['score']:3}")

print("\nTop 5")

for c in result["top5"]:
    print(c)

print("\nRecommendation")
print(result["recommendation"])

# ---------------------------------------------------
# Save Markdown Report
# ---------------------------------------------------

Path("outputs").mkdir(exist_ok=True)

report = "# AI HR Screening Report\n\n"

report += "## Job Summary\n\n"

report += result["summary"] + "\n\n"

report += "| Candidate | Score | Remarks |\n"
report += "|-----------|------:|---------|\n"

for c in result["candidates"]:

    report += f"| {c['name']} | {c['score']} | {c['remarks']} |\n"

report += "\n## Top 5 Candidates\n\n"

for c in result["top5"]:
    report += f"- {c}\n"

report += "\n## Recommendation\n\n"

report += result["recommendation"]

Path("outputs/report.md").write_text(
    report,
    encoding="utf-8"
)

# ---------------------------------------------------
# Plot Scores
# ---------------------------------------------------

names = [c["name"] for c in result["candidates"]]
scores = [c["score"] for c in result["candidates"]]

plt.figure(figsize=(10,5))
plt.bar(names, scores)

plt.title("Candidate Scores")

plt.xlabel("Candidate")

plt.ylabel("Score")

plt.ylim(0,100)

plt.tight_layout()

plt.savefig("outputs/scores.png")

plt.show()

print("\nReport saved to outputs/report.md")
print("Chart saved to outputs/scores.png")