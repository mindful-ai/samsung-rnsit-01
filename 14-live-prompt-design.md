# Prompt Engineering Progression Example

# Theme
**Generate a Table of Contents for an "AI Mastery" Course**

This example demonstrates how prompt quality improves by progressively adding more context and structure.

---

# Stage 1 – Bad Prompt

## Prompt

```text
Create a table of contents for AI Mastery.
```

## Typical Output

```text
1. Introduction
2. Machine Learning
3. Deep Learning
4. Neural Networks
5. NLP
6. Computer Vision
7. AI Ethics
8. Conclusion
```

## Problems

- Too generic
- No target audience
- Missing important topics
- No logical learning path
- No practical orientation

---

# Stage 2 – Structured Prompt

## Components Added

- Role
- Goal
- Context
- Constraints
- Style
- Output Format

## Prompt

```text
Role:
You are an AI curriculum designer.

Goal:
Create a comprehensive table of contents for an AI Mastery course.

Context:
The course is intended for software engineers who want to become AI engineers.

Constraints:
- Beginner to advanced
- Cover Generative AI and Agentic AI
- Maximum 15 modules

Style:
Professional and industry-oriented.

Output Format:
Return a numbered table of contents.
```

## Typical Output

```text
1. AI Fundamentals
2. Python for AI
3. Machine Learning
4. Deep Learning
5. Transformers
6. Prompt Engineering
7. Retrieval-Augmented Generation
8. AI Agents
9. Multi-Agent Systems
10. Computer Vision
11. NLP
12. AI Deployment
13. Responsible AI
14. AI Projects
15. Capstone Project
```

## Improvements

- Better organization
- Logical progression
- Relevant audience
- Modern AI topics

---

# Stage 3 – Add Learning Context, Negative Prompting, and Verification

## Additional Components

- Learning Domain Context
- Negative Prompting
- Verification Techniques

## Prompt

```text
Role:
You are a senior AI curriculum architect.

Goal:
Design an industry-ready AI Mastery curriculum.

Learning Domain Context:
The learners are software engineers with Python knowledge who want to become AI engineers within 6 months.

Constraints:
- Beginner to advanced
- Maximum 15 modules
- Emphasize hands-on learning
- Include projects after major topics

Negative Prompting:
- Do not include outdated AI topics.
- Do not repeat topics.
- Do not include unnecessary mathematics.
- Avoid vague module names.

Verification:
Before producing the answer:
- Verify logical learning order.
- Ensure no duplicate topics.
- Ensure every module contributes to job readiness.
- Check that prerequisites appear before advanced topics.

Style:
Professional and practical.

Output Format:
Return a numbered table with:
- Module
- Learning Outcome
- Mini Project
```

## Typical Output

| Module | Learning Outcome | Mini Project |
|---------|------------------|--------------|
| AI Foundations | Understand modern AI | AI terminology chatbot |
| Python for AI | AI-ready Python | Data processing toolkit |
| Machine Learning | Predictive models | House price predictor |
| Deep Learning | Neural networks | Image classifier |
| Transformers | LLM architecture | Transformer visualization |
| Prompt Engineering | Effective prompting | Prompt library |
| RAG | Document Q&A | PDF chatbot |
| AI Agents | Autonomous agents | Personal AI assistant |
| Multi-Agent Systems | Agent collaboration | Research assistant |
| Computer Vision | Image understanding | Object detector |
| NLP | Text processing | Sentiment analyzer |
| AI Deployment | Production deployment | FastAPI deployment |
| Responsible AI | Ethics and governance | AI risk assessment |
| End-to-End Projects | Integrated AI systems | Enterprise AI solution |
| Capstone | Production-ready AI application | Portfolio project |

## Improvements

- Audience-specific curriculum
- Hands-on learning path
- Industry-ready topics
- Self-verified logical sequence
- Structured and consistent output

---

# Summary

| Stage | Prompt Characteristics | Result |
|-------|------------------------|--------|
| Stage 1 | Simple request | Generic output |
| Stage 2 | Role, Goal, Context, Constraints, Style, Output Format | Organized and relevant output |
| Stage 3 | Learning Context, Negative Prompting, Verification | High-quality, reliable, industry-ready output |

# Key Takeaway

As additional prompt engineering techniques are applied, the AI produces responses that are progressively more accurate, structured, relevant, and useful. Effective prompting transforms a vague request into a well-defined specification that guides the AI toward high-quality results.


# Finalized prompts

```text
ROLE:
You are an expert curriculum designer

GOAL:
Create a comprehensive table of contents for an AI Mastery course

CONTEXT:
This course is intended for third year Computer Science engineering students

CONSTRAINTS:
- Beginner to Advanced
- Cover Python for Data Science, ML, DL, Generative and Agentic AI
- Maximum 20 modules
- Overall time 200 hours
- Student can afford to spend 5 hours in a week


STYLE:
Profession and industry standard

OUTPUT FORMAT:
Return
    - Table with 4 columns: topic number, topic, sub-topics, recommended hands-on
    - Give a daily plan 
```