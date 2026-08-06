# AI Research Paper Summarizer

## Classroom Exercise

**Duration:** 60 Minutes

**Difficulty:** Beginner

**Programming Language:** Python

**LLM:** Groq

---

# Objective

Researchers and students often need to quickly understand research papers before deciding whether to read them in detail.

Develop an **AI Research Paper Summarizer** that can summarize a research paper from either:

1. A local PDF file
2. A PubMed article URL

The application should extract the paper text and generate an easy-to-understand summary.

---

# Learning Objectives

By completing this exercise, students will learn to:

- Read PDF files
- Accept URLs as input
- Extract text from research papers
- Build effective prompts
- Call the Groq API
- Generate structured summaries

---

# Problem Statement

Create a Python application that allows the user to choose one of two input methods.

Option 1:
Read a research paper from a local PDF file.

Option 2:
Read a research paper using a PubMed URL such as

https://pubmed.ncbi.nlm.nih.gov/12345678/

For PubMed articles, students may summarize the abstract (always available when present) or, when full text is openly available, retrieve the linked full text. PubMed pages provide article metadata, abstracts, and links to full-text resources when available. :contentReference[oaicite:0]{index=0}

The application should then generate an AI summary.

---

# Functional Requirements

The AI should generate

- Paper Title
- Authors (if available)
- Research Domain
- Research Objective
- Problem Statement
- Methodology
- Dataset (if available)
- Key Findings
- Advantages
- Limitations
- Future Work
- Practical Applications
- Simple Explanation (ELI5)
- Overall Summary (200 words)

---

# Input

The application should first ask:

```text
Choose Input Source

1. PDF File

2. PubMed URL
```

If PDF

```text
Enter PDF path:
```

If PubMed

```text
Enter PubMed URL:
```

Example

```text
https://pubmed.ncbi.nlm.nih.gov/40721878/
```

---

# Expected Output

```text
==========================================================
AI RESEARCH PAPER SUMMARY
==========================================================

Paper Title
-----------
Attention Is All You Need

Authors
-------
Ashish Vaswani et al.

Research Domain
---------------
Natural Language Processing

Research Objective
------------------
Introduce a transformer architecture that removes recurrence
from sequence modeling.

Methodology
-----------
Transformer Encoder-Decoder
Self Attention
Multi-Head Attention

Key Findings
------------
• Faster training
• Better translation accuracy
• Highly parallelizable

Advantages
----------
• Faster
• Scalable
• Better performance

Limitations
-----------
• Large datasets required
• High computational cost

Future Work
-----------
Large language models
Vision transformers

Applications
------------
Machine Translation
Chatbots
Text Summarization

Simple Explanation
------------------
Imagine every word in a sentence can directly "look at"
every other word before making a decision.

Overall Summary
---------------
The paper introduces the Transformer architecture...
```

---

# Suggested Prompt

```text
You are an experienced research scientist.

Analyze the following research paper.

Provide:

1. Paper Title
2. Authors
3. Research Domain
4. Research Objective
5. Problem Statement
6. Methodology
7. Dataset Used
8. Key Findings
9. Advantages
10. Limitations
11. Future Work
12. Practical Applications
13. Explain Like I'm 15
14. Overall Summary

Write in simple English.

Use headings and bullet points.
```

---

# Suggested Folder Structure

```text
research-paper-summarizer/
│
├── main.py
├── requirements.txt
├── sample.pdf
├── groq-api.key
└── README.md
```

---

# Recommended Python Packages

```bash
pip install groq
pip install pymupdf
pip install requests
pip install beautifulsoup4
```

---

# Expected Skills

Students should demonstrate the ability to

- Read PDF documents
- Parse web pages
- Extract text
- Build prompts
- Use Groq API
- Handle exceptions

---

# Bonus Challenges

Students can extend the application to

- Export summary to Markdown
- Export summary to PDF
- Generate PowerPoint slides
- Create quiz questions
- Generate interview questions
- Compare two research papers
- Extract references
- Generate citation in APA format
- Chat with the paper using RAG

---

# Deliverables

Students should submit

- main.py
- requirements.txt
- README.md
- Sample PDF
- Screenshot of execution

---

# Evaluation Criteria

| Criteria | Marks |
|----------|------:|
| PDF/Text Extraction | 20 |
| PubMed Processing | 20 |
| Groq API | 20 |
| Prompt Design | 15 |
| Output Formatting | 15 |
| Code Quality | 10 |

**Total: 100 Marks**

---

# Outcome

Students will build an AI-powered research paper summarizer capable of accepting either a PDF document or a PubMed article URL, extracting the available content, and producing a structured summary using a Large Language Model.