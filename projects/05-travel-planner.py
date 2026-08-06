"""
AI Travel & Itinerary Planner

Requirements:
pip install groq
"""

from groq import Groq

# ----------------------------------------------------
# Load API Key
# ----------------------------------------------------

KEY_PATH = r"samsung-ai\key-vault\groq-api.key"

with open(KEY_PATH, "r") as f:
    api_key = f.read().strip()

client = Groq(api_key=api_key)

# ----------------------------------------------------
# User Inputs
# ----------------------------------------------------

destination = input("Destination: ")
days = input("Number of days: ")
budget = input("Budget (₹): ")
travellers = input("Number of travellers: ")
style = input("Travel Style (Family/Solo/Couple/Friends): ")

# ----------------------------------------------------
# Prompt
# ----------------------------------------------------

prompt = f"""
You are an experienced travel planner.

Create a personalized travel itinerary.

Destination:
{destination}

Duration:
{days} days

Budget:
₹{budget}

Travellers:
{travellers}

Travel Style:
{style}

Provide the response using the following headings:

1. Destination Overview
2. Best Time to Visit
3. Day-wise Itinerary
4. Tourist Attractions
5. Local Food Recommendations
6. Transportation Options
7. Budget-Friendly Accommodation Suggestions
8. Estimated Budget Breakdown
9. Packing Checklist
10. Safety Tips

Keep the recommendations practical, budget-conscious, and easy to follow.
"""

# ----------------------------------------------------
# Call Groq
# ----------------------------------------------------

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.4,
)

# ----------------------------------------------------
# Display Output
# ----------------------------------------------------

print("\n" + "=" * 70)
print("AI TRAVEL & ITINERARY PLANNER")
print("=" * 70)
print(response.choices[0].message.content)