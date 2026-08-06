# AI Schedule Optimizer using Groq LLM

## Workshop Duration

60 Minutes

---

# Objective

Develop a Python application that uses a Large Language Model (LLM) hosted on Groq to solve scheduling and planning problems.

The application should read a problem statement from a Markdown (.md) or plain text (.txt) file and ask the LLM to generate the best possible schedule while satisfying all constraints.

The application uses the ReAct prompting technique to guide the reasoning process.

---

# Learning Objectives

After completing this workshop, students will be able to

- Read files using Python
- Use the Groq Python SDK
- Build prompts
- Call an LLM
- Save AI-generated responses
- Generate Markdown reports

---

# Functional Requirements

The application shall

1. Read a problem statement from

   - Markdown (.md)

   OR

   - Plain Text (.txt)

2. Send the complete problem to the LLM.

3. Ask the LLM to

   - Understand the problem
   - Identify constraints
   - Identify dependencies
   - Build a feasible schedule
   - Maximize the objective
   - Compute the total score

4. Display the generated solution.

5. Save the solution as

outputs/solution.md

---

# Input

The input can be any scheduling problem.

Example

- Student Assignment Planning
- Factory Scheduling
- Hospital Planning
- Software Sprint Planning

---

# Output

The LLM should generate the following sections.

# Constraint Summary

# Dependencies

# Critical Path

# Optimized Schedule

# Objective Score

# Suggestions

---

# Folder Structure

AI-Scheduler/

│

├── app.py

├── requirements.txt

├── .env

│

├── inputs/

│      assignment.md

│

└── outputs/

       solution.md

---

# Requirements

Python 3.11+

groq

python-dotenv

---

# Evaluation (100 Marks)

Reading Input File ............. 10

Groq API Integration ........... 25

Prompt Engineering ............. 20

Output Formatting .............. 20

Saving Markdown Output ......... 15

Code Quality ................... 10

---

# Bonus

If time permits

- Ask user for input filename
- Choose different Groq models
- Display execution time
- Add colored terminal output