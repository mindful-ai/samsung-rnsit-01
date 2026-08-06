"""
AI Tax Saving Advisor
Single File Workshop Solution

pip install groq python-dotenv matplotlib
"""

import os
import json
from pathlib import Path
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.1-8b-instant"

profile = Path("inputs/person_profile.md").read_text(encoding="utf-8")

prompt = f"""
You are an experienced Chartered Accountant and Financial Advisor.

Analyze the following financial profile.

{profile}

Return ONLY valid JSON.

{{
"financial_summary":"",

"old_regime":{{
    "estimated_tax":0,
    "remarks":""
}},

"new_regime":{{
    "estimated_tax":0,
    "remarks":""
}},

"recommended_regime":"",

"deductions":[
{{
"name":"",
"status":"Fully Utilized / Partial / Not Utilized",
"limit":"",
"current":"",
"remaining":"",
"remarks":""
}}
],

"recommendations":[
{{
"category":"",
"section":"",
"investment":0,
"estimated_tax_saving":0,
"priority":"",
"remarks":""
}}
],

"investment_mix":[
{{
"instrument":"",
"percentage":0
}}
],

"action_plan":[
"",
"",
""
]
}}
"""

response = client.chat.completions.create(
    model=MODEL,
    temperature=0.2,
    messages=[{"role":"user","content":prompt}]
)

result = json.loads(response.choices[0].message.content)

Path("outputs").mkdir(exist_ok=True)

# -------------------------------
# Markdown Report
# -------------------------------

report = "# AI Tax Saving Report\n\n"

report += "## Financial Summary\n\n"
report += result["financial_summary"] + "\n\n"

report += "## Tax Regime Comparison\n\n"

report += "| Regime | Estimated Tax |\n"
report += "|---------|--------------:|\n"
report += f"| Old | ₹{result['old_regime']['estimated_tax']} |\n"
report += f"| New | ₹{result['new_regime']['estimated_tax']} |\n\n"

report += f"**Recommended Regime:** {result['recommended_regime']}\n\n"

report += "## Deduction Utilization\n\n"

report += "| Deduction | Status | Remaining |\n"
report += "|------------|--------|----------:|\n"

for d in result["deductions"]:
    report += f"| {d['name']} | {d['status']} | {d['remaining']} |\n"

report += "\n## Recommendations\n\n"

report += "| Category | Section | Tax Saving |\n"
report += "|-----------|---------|-----------:|\n"

for r in result["recommendations"]:
    report += f"| {r['category']} | {r['section']} | ₹{r['estimated_tax_saving']} |\n"

report += "\n## Suggested Investment Mix\n\n"

for inv in result["investment_mix"]:
    report += f"- {inv['instrument']} : {inv['percentage']}%\n"

report += "\n## Action Plan\n\n"

for step in result["action_plan"]:
    report += f"- {step}\n"

Path("outputs/Tax_Report.md").write_text(report, encoding="utf-8")

# -------------------------------
# Chart 1
# Tax Saving by Category
# -------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    [r["category"] for r in result["recommendations"]],
    [r["estimated_tax_saving"] for r in result["recommendations"]]
)

plt.title("Estimated Tax Saving by Category")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("outputs/tax_saving_chart.png")
plt.close()

# -------------------------------
# Chart 2
# Investment Mix
# -------------------------------

plt.figure(figsize=(6,6))

plt.pie(
    [i["percentage"] for i in result["investment_mix"]],
    labels=[i["instrument"] for i in result["investment_mix"]],
    autopct="%1.1f%%"
)

plt.title("Suggested Investment Mix")
plt.savefig("outputs/investment_mix.png")
plt.close()

# -------------------------------
# Chart 3
# Old vs New
# -------------------------------

plt.figure(figsize=(5,5))

plt.bar(
    ["Old","New"],
    [
        result["old_regime"]["estimated_tax"],
        result["new_regime"]["estimated_tax"]
    ]
)

plt.title("Estimated Tax Comparison")
plt.savefig("outputs/tax_regime_comparison.png")
plt.close()

print("\nReport generated successfully.")
print("Files are available in the outputs folder.")