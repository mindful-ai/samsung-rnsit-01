# AI Travel and Itinerary Planner

## Classroom Exercise

**Duration:** 60 Minutes

**Difficulty:** Beginner

**Programming Language:** Python

**LLM:** Groq

---

# Objective

Planning a trip involves researching destinations, attractions, transportation, accommodation, and budgeting. Build an **AI Travel and Itinerary Planner** that generates a personalized travel itinerary based on user preferences.

The application should create a day-wise travel plan and provide useful travel recommendations.

---

# Learning Objectives

By completing this exercise, students will learn to:

- Read user input
- Build structured prompts
- Call the Groq API
- Generate AI-powered travel recommendations
- Format AI responses for readability

---

# Problem Statement

Develop a Python application that accepts travel preferences from the user and generates a complete travel itinerary.

The application should perform the following tasks:

1. Ask the user for:
   - Destination
   - Number of days
   - Budget
   - Number of travelers
   - Preferred travel style
2. Send the information to the Groq LLM.
3. Display a detailed travel itinerary.

---

# Functional Requirements

The AI should generate:

- Destination Overview
- Best Time to Visit
- Day-wise Itinerary
- Recommended Tourist Attractions
- Local Food Suggestions
- Transportation Options
- Accommodation Suggestions
- Estimated Budget Breakdown
- Packing Tips
- Travel Safety Tips

---

# Sample Input

```text
Destination : Mysore
Days        : 2
Budget      : ₹10000
Travellers  : 2
Travel Style: Family
```

---

# Expected Output

```text
======================================================
AI TRAVEL PLAN
======================================================

Destination
-----------
Mysore

Overview
--------
Mysore is famous for its royal heritage, palaces,
gardens, and rich cultural traditions.

Best Time
----------
October to February

Day 1
-----
• Mysore Palace
• St. Philomena's Church
• Mysore Zoo
• Evening at Brindavan Gardens

Day 2
-----
• Chamundi Hills
• Nandi Statue
• Jaganmohan Palace
• Local Shopping

Recommended Food
----------------
• Mysore Masala Dosa
• Mysore Pak
• Filter Coffee

Transportation
--------------
Auto
Cab
City Bus

Budget Estimate
---------------
Hotel      : ₹3500
Food       : ₹2000
Travel     : ₹1500
Tickets    : ₹1000
Shopping   : ₹2000

Packing Tips
------------
• Comfortable shoes
• Water bottle
• Umbrella

Safety Tips
-----------
• Carry ID proof.
• Stay hydrated.
• Follow local regulations.
```

---

# Suggested Prompt

Use a prompt similar to the following:

```text
You are an experienced travel planner.

Create a personalized travel itinerary.

Destination:
{destination}

Duration:
{days} days

Budget:
{budget}

Travellers:
{travellers}

Travel Style:
{style}

Provide:

1. Destination overview
2. Best season to visit
3. Day-wise itinerary
4. Tourist attractions
5. Local food recommendations
6. Transportation
7. Hotel suggestions (budget friendly)
8. Estimated budget breakdown
9. Packing checklist
10. Safety tips

Keep the itinerary practical and beginner-friendly.
```

---

# Suggested Folder Structure

```text
travel-planner/
│
├── main.py
├── requirements.txt
├── groq-api.key
└── README.md
```

---

# Recommended Python Packages

```bash
pip install groq
```

---

# Expected Skills

Students should demonstrate the ability to:

- Read multiple user inputs
- Construct prompts
- Use the Groq API
- Format AI-generated responses
- Handle invalid input

---

# Bonus Challenges

Students can extend the application to:

- Suggest nearby tourist attractions.
- Estimate total trip cost.
- Generate a packing checklist based on weather.
- Recommend restaurants.
- Export itinerary to Markdown.
- Export itinerary to PDF.
- Create a PowerPoint itinerary.
- Generate a Google Maps places list.
- Translate the itinerary into another language.

---

# Deliverables

Students should submit:

- main.py
- requirements.txt
- README.md
- Screenshot of execution

---

# Evaluation Criteria

| Criteria | Marks |
|-----------|------:|
| User Input | 15 |
| Groq API Integration | 20 |
| Prompt Engineering | 20 |
| Output Formatting | 15 |
| Error Handling | 10 |
| Code Quality | 20 |

**Total:** **100 Marks**

---

# Outcome

At the end of this exercise, students will have developed an AI-powered travel planning assistant capable of generating personalized itineraries using Python and Groq LLMs.