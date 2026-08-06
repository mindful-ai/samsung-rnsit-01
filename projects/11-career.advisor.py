"""
AI Career Advisor

Requirements

pip install groq rich

Set

GROQ_API_KEY=<your key>
"""

import os
import json

from groq import Groq
from rich.console import Console
from rich.table import Table

console = Console()

SYSTEM_PROMPT = """
You are an experienced Career Advisor.

Your task is to recommend suitable careers.

Return ONLY valid JSON.

Schema:

{
  "recommended_careers":[
    {
      "career":"",
      "suitability_score":0,
      "reason":""
    }
  ],
  "skills_to_learn":[],
  "recommended_certifications":[],
  "learning_resources":[],
  "roadmap":[],
  "estimated_transition_time":""
}
"""

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    console.print("[red]Please set GROQ_API_KEY[/red]")
    raise SystemExit()

client = Groq(api_key=api_key)

profile = console.input(
    "[bold cyan]Describe your education, skills and career goals:[/bold cyan]\n"
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    response_format={"type":"json_object"},
    messages=[
        {
            "role":"system",
            "content":SYSTEM_PROMPT
        },
        {
            "role":"user",
            "content":profile
        }
    ]
)

data = json.loads(response.choices[0].message.content)

table = Table(title="Career Recommendations")

table.add_column("Career", style="cyan")
table.add_column("Score")
table.add_column("Reason", style="green")

for career in data["recommended_careers"]:
    table.add_row(
        career["career"],
        str(career["suitability_score"]),
        career["reason"]
    )

console.print(table)

console.print("\n[bold yellow]Skills to Learn[/bold yellow]")

for skill in data["skills_to_learn"]:
    console.print(f"• {skill}")

console.print("\n[bold yellow]Recommended Certifications[/bold yellow]")

for cert in data["recommended_certifications"]:
    console.print(f"• {cert}")

console.print("\n[bold yellow]Learning Resources[/bold yellow]")

for resource in data["learning_resources"]:
    console.print(f"• {resource}")

console.print("\n[bold yellow]Learning Roadmap[/bold yellow]")

for step in data["roadmap"]:
    console.print(f"• {step}")

console.print(
    f"\n[bold green]Estimated Transition Time:[/bold green] "
    f"{data['estimated_transition_time']}"
)