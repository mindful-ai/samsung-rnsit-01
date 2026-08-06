# AI Podcast Summarizer

## Classroom Exercise

**Duration:** 60 Minutes

**Difficulty:** Beginner

**Programming Language:** Python

**Speech-to-Text:** Groq Whisper

**LLM:** Groq Llama 3.1

---

# Objective

Podcasts often contain valuable information but can be lengthy.

Develop an AI-powered Podcast Summarizer that converts speech into text using Groq Whisper and then uses a Large Language Model to generate a structured summary.

---

# Learning Objectives

Students will learn to

- Upload audio files
- Perform Speech-to-Text
- Use Groq Whisper API
- Use Groq LLM
- Prompt engineering
- AI summarization
- File handling

---

# Problem Statement

Develop a Python application that accepts a podcast audio file and automatically generates a structured summary.

---

# Functional Requirements

The application should

1. Ask the user to enter the podcast filename.
2. Transcribe the podcast using Groq Whisper.
3. Summarize the transcript using Groq LLM.
4. Display the results.

---

# Supported Audio Formats

- MP3
- WAV
- FLAC
- M4A
- OGG

---

# Output

The application should generate

- Podcast Title (if identifiable)
- Summary
- Five Key Points
- Important Keywords
- Main Topics
- Action Items
- Target Audience
- Sentiment
- One-line Takeaway

---

# Sample Input

```text
Podcast File

ai-podcast.mp3
```

---

# Sample Output

```text
=================================================
AI PODCAST SUMMARY
=================================================

Podcast
-------
Future of Artificial Intelligence

Summary
-------
...

Key Points
----------
• ...
• ...
• ...

Keywords
--------
AI
LLM
Automation

Topics
------
Machine Learning
Prompt Engineering
Agentic AI

Action Items
------------
• Learn Python
• Build AI projects

Sentiment
---------
Positive

Target Audience
---------------
Students
Developers

Takeaway
--------
AI is transforming software development.
```

---

# Suggested Prompt

```
You are an expert podcast reviewer.

Analyze the podcast transcript.

Provide

1. Summary
2. Five key points
3. Keywords
4. Main topics
5. Action items
6. Target audience
7. Sentiment
8. One-line takeaway

Write in simple English.
```

---

# Folder Structure

```
podcast-summarizer/

│
├── main.py
├── sample.mp3
├── requirements.txt
├── groq-api.key
└── README.md
```

---

# Packages

```bash
pip install groq
```

---

# Bonus Challenges

Students can extend the project by adding

- Translation
- PDF report
- Markdown report
- Blog generation
- Quiz generation
- Meeting minutes
- Speaker identification
- Chat with podcast
- Timestamp extraction

---

# Deliverables

- main.py
- requirements.txt
- README.md
- Sample audio
- Screenshot

---

# Evaluation

| Criteria | Marks |
|----------|------:|
| Speech-to-Text | 25 |
| Groq API | 20 |
| Prompt Design | 20 |
| Output | 15 |
| Error Handling | 10 |
| Code Quality | 10 |

Total = 100 Marks

---

# Outcome

Students will build a complete multimodal AI application that combines Speech-to-Text and Large Language Models using Groq APIs.