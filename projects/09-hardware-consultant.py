"""
Mobile and Computer Configuration Suggestor
pip install groq rich
Set GROQ_API_KEY before running.
"""

import os
import json
from groq import Groq
from rich.console import Console
from rich.table import Table

console = Console()

SYSTEM_PROMPT = """
You are an expert hardware consultant.

Recommend mobile phones, laptops or desktop configurations.

Return ONLY valid JSON using this schema:

{
 "device_type":"",
 "recommended_configuration":{
   "processor":"",
   "ram":"",
   "storage":"",
   "gpu":"",
   "display":"",
   "battery":""
 },
 "price_range":"",
 "recommended_models":[],
 "reason":""
}
"""

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    console.print("[red]Please set GROQ_API_KEY[/red]")
    raise SystemExit()

client = Groq(api_key=api_key)

req = console.input("[cyan]Describe your requirements: [/cyan]")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    response_format={"type":"json_object"},
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":req}
    ]
)

data = json.loads(response.choices[0].message.content)

table = Table(title="Recommended Configuration")
table.add_column("Item", style="cyan")
table.add_column("Value", style="green")

table.add_row("Device", data["device_type"])

for k, v in data["recommended_configuration"].items():
    if v:
        table.add_row(k.capitalize(), str(v))

table.add_row("Price Range", data["price_range"])
table.add_row("Models", ", ".join(data["recommended_models"]))
table.add_row("Reason", data["reason"])

console.print(table)
