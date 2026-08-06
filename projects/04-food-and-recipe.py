from groq import Groq

KEY_PATH = r"samsung-ai\key-vault\groq-api.key"

with open(KEY_PATH) as f:
    api_key = f.read().strip()

client = Groq(api_key=api_key)

ingredients = input("Enter available ingredients:\n")

diet = input("Diet (Veg/Non-Veg/Vegan): ")

cuisine = input("Cuisine (Indian/Chinese/etc): ")

prompt = f"""
You are an expert chef.

Available ingredients:

{ingredients}

Diet:

{diet}

Cuisine:

{cuisine}

Create a recipe.

Provide:

- Recipe Name
- Ingredients Used
- Missing Ingredients
- Preparation Time
- Cooking Time
- Cooking Steps
- Nutrition Summary
- Serving Suggestions
"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
)

print(response.choices[0].message.content)