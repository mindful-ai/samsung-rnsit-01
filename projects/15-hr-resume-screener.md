# AI HR Resume Screening Assistant using Groq

## Workshop Duration

60 Minutes

---

# Objective

Develop an AI-powered HR Assistant using Python and the Groq LLM.

The application reads

- One Job Description (Markdown or Text)
- Multiple Candidate Profiles (Markdown or Text)

The application asks the LLM to analyze all candidate profiles, compare them against the job description, rank the candidates, and recommend the Top 5.

The application should also generate a score for every candidate and visualize the results using a bar chart.

---

# Learning Objectives

Students will learn to

- Read multiple files
- Use Python file handling
- Use the Groq API
- Build effective prompts
- Perform semantic document comparison
- Generate structured AI reports
- Visualize AI outputs using Matplotlib

---

# Functional Requirements

The application shall

1. Read one Job Description

2. Read multiple candidate profile files

3. Send all documents to the LLM

4. Ask the LLM to

    • Compare every profile with the Job Description

    • Evaluate

        - Technical Skills

        - Experience

        - Education

        - Certifications

        - Domain Knowledge

        - Soft Skills

    • Give a score out of 100

    • Explain the score

    • Rank every candidate

    • Recommend Top 5 candidates

5. Display the ranking.

6. Save the report as Markdown.

7. Generate a bar chart showing candidate scores.

---

# Input

Job Description

inputs/job_description.md

Candidate Profiles

inputs/profiles/

    candidate1.md

    candidate2.md

    candidate3.md

    ...

---

# Output

The report must contain

# Job Summary

# Candidate Evaluation

| Candidate | Score | Remarks |

# Top 5 Candidates

# Hiring Recommendation

---

# Folder Structure

HR-Assistant/

│

├── app.py

├── requirements.txt

├── .env

│

├── inputs/

│      job_description.md

│

├── inputs/profiles/

│      candidate1.md

│      candidate2.md

│      ...

│

└── outputs/

       report.md

       scores.png

---

# Evaluation

File Handling................10

Groq Integration.............25

Prompt Engineering...........25

Candidate Ranking............20

Chart Generation.............20

Total.......................100