# AI Text Translation and Summarization Assistant

## Classroom Exercise

**Duration:** 60 Minutes

**Difficulty:** Beginner

**Programming Language:** Python

**LLM:** Groq

---

# Objective

People often need to translate text into different languages or summarize lengthy documents.

Develop an **AI Text Translation and Summarization Assistant** that performs either translation or summarization based on the user's choice.

---

# Learning Objectives

By completing this exercise, students will learn to:

- Read multi-line text input
- Build prompts dynamically
- Use the Groq API
- Perform machine translation
- Generate concise summaries
- Format AI-generated output

---

# Problem Statement

Create a Python application that performs the following steps:

1. Ask the user to choose an operation:
   - Translate Text
   - Summarize Text
2. Accept multi-line text input.
3. If translation is selected:
   - Ask for the target language.
   - Translate the text.
4. If summarization is selected:
   - Generate a concise summary.
5. Display the AI-generated result.

---

# Functional Requirements

## Translation Mode

The application should:

- Detect the source language (if possible)
- Translate to the requested language
- Preserve formatting
- Preserve names and technical terms where appropriate

Supported examples:

- English → Hindi
- English → Kannada
- English → Tamil
- English → Telugu
- English → French
- English → German
- English → Japanese
- English → Spanish

---

## Summarization Mode

Generate:

- Short Summary
- Five Key Points
- Important Keywords
- Target Audience
- One-Sentence Summary

---

# Sample Input

```
Choose Operation

1. Translate

2. Summarize

Choice: 1

Target Language:

Kannada

Enter Text:

Artificial Intelligence is transforming education.
```

---

# Sample Output

```
===================================================
TRANSLATION
===================================================

Detected Language
-----------------
English

Target Language
---------------
Kannada

Translation
-----------
ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ ಶಿಕ್ಷಣ ಕ್ಷೇತ್ರವನ್ನು ಪರಿವರ್ತಿಸುತ್ತಿದೆ.
```

---

# Sample Input (Summarization)

```
Choice: 2

Enter Text:

<Large article>
```

---

# Sample Output

```
===================================================
SUMMARY
===================================================

Summary
-------
...

Key Points
----------
• Point 1
• Point 2
• Point 3
• Point 4
• Point 5

Keywords
---------
AI
Machine Learning
Education

Target Audience
---------------
Students

One-line Summary
----------------
Artificial Intelligence is changing education.
```

---

# Suggested Prompt (Translation)

```
You are a professional translator.

Translate the following text into the specified language.

Target Language:
{language}

Requirements:

- Preserve formatting
- Preserve names
- Preserve technical terms when appropriate
- Do not add explanations

Text:

{text}
```

---

# Suggested Prompt (Summarization)

```
You are an expert editor.

Summarize the following text.

Provide:

1. Summary (150 words)
2. Five key points
3. Important keywords
4. Target audience
5. One-sentence summary

Write in simple English.
```

---

# Suggested Folder Structure

```
text-assistant/
│
├── main.py
├── requirements.txt
├── groq-api.key
└── README.md
```

---

# Recommended Packages

```bash
pip install groq
```

---

# Expected Skills

Students should demonstrate the ability to:

- Read multi-line input
- Build prompts
- Use the Groq API
- Display formatted responses
- Handle invalid choices gracefully

---

# Bonus Challenges

Students can extend the application to:

- Auto-detect language
- Translate into multiple languages simultaneously
- Summarize in bullet points only
- Summarize to a user-specified length
- Export translation to Markdown
- Export summary to PDF
- Read text from a file
- Translate Markdown while preserving formatting
- Translate and summarize in a single workflow

---

# Deliverables

Students should submit:

- main.py
- requirements.txt
- README.md
- Sample execution screenshots

---

# Evaluation Criteria

| Criteria | Marks |
|----------|------:|
| User Input | 15 |
| Prompt Engineering | 20 |
| Groq API Integration | 20 |
| Translation/Summarization | 20 |
| Output Formatting | 15 |
| Code Quality | 10 |

**Total: 100 Marks**

---

# Outcome

Students will build an AI-powered NLP application capable of translating text into multiple languages and generating structured summaries using Groq-powered Large Language Models.