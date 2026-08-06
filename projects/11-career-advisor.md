# Project: AI Career Advisor

## Objective

Develop an AI-powered Career Advisor that recommends suitable career paths based on a user's profile, interests, skills, education, and career goals.

The assistant should provide personalized career recommendations, required skills, learning roadmap, and suggested certifications.

---

# Problem Statement

Build a Python application that accepts a user's profile in natural language and recommends suitable career options.

The application should help students and professionals identify potential career paths based on their background and aspirations.

---

# Functional Requirements

The application shall:

1. Accept user information.
2. Understand career goals.
3. Recommend suitable careers.
4. Explain why each career is suitable.
5. Suggest skills to acquire.
6. Recommend certifications.
7. Suggest learning resources.
8. Generate a learning roadmap.
9. Return structured JSON.

---

# Input

The user may provide:

- Education
- Current profession
- Skills
- Interests
- Preferred industry
- Experience
- Career goal

Example

"I am a Mechanical Engineer with 3 years experience.
I know Python and SQL.
I enjoy problem solving and AI.
I want to transition into Data Science."

---

# Output

The AI should provide:

- Career Recommendations
- Suitability Score
- Reasons
- Skills to Learn
- Certifications
- Learning Roadmap
- Estimated Transition Time

---

# JSON Schema

```json
{
  "recommended_careers": [
    {
      "career": "",
      "suitability_score": 0,
      "reason": ""
    }
  ],
  "skills_to_learn": [],
  "recommended_certifications": [],
  "learning_resources": [],
  "roadmap": [],
  "estimated_transition_time": ""
}
```

---

# Technical Requirements

- Python
- Groq API
- JSON Output
- Rich Console

---

# Future Enhancements

- Resume Upload
- LinkedIn Profile Analysis
- Skill Gap Analysis
- Salary Estimation
- Job Recommendation
- Streamlit Interface