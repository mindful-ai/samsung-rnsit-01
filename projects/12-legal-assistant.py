"""
AI Legal Consultant

Requirements

pip install groq rich

Set:

GROQ_API_KEY=<your key>
"""

import os
import json

from groq import Groq
from rich.console import Console
from rich.table import Table

console = Console()

SYSTEM_PROMPT = """
You are an experienced legal consultant.

Provide GENERAL LEGAL INFORMATION ONLY.

Never claim to be a lawyer.

Never provide definitive legal advice.

Always recommend consulting a qualified legal professional for important legal matters.

Return ONLY valid JSON.

Schema:

{
    "legal_topic":"",
    "summary":"",
    "important_points":[],
    "possible_considerations":[],
    "suggested_next_steps":[],
    "disclaimer":""
}
"""

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    console.print("[red]Please set GROQ_API_KEY[/red]")
    raise SystemExit()

client = Groq(api_key=api_key)

query = console.input(
    "[bold cyan]Enter your legal question:[/bold cyan] "
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": query
        }
    ]
)

data = json.loads(
    response.choices[0].message.content
)

table = Table(title="AI Legal Consultant")

table.add_column("Item", style="cyan", width=25)
table.add_column("Information", style="green")

table.add_row(
    "Legal Topic",
    data["legal_topic"]
)

table.add_row(
    "Summary",
    data["summary"]
)

table.add_row(
    "Important Points",
    "\n".join(data["important_points"])
)

table.add_row(
    "Legal Considerations",
    "\n".join(data["possible_considerations"])
)

table.add_row(
    "Suggested Next Steps",
    "\n".join(data["suggested_next_steps"])
)

table.add_row(
    "Disclaimer",
    data["disclaimer"]
)

console.print(table)