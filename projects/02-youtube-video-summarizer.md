# AI YouTube Video Summarizer

## Classroom Exercise

**Duration:** 60 Minutes

**Difficulty:** Beginner

**Programming Language:** Python

**LLM:** Groq

---

# Objective

Watching lengthy YouTube videos can be time-consuming. Build an **AI YouTube Video Summarizer** that accepts a YouTube video URL, extracts the transcript, and uses a Large Language Model (LLM) to generate a concise, structured summary.

This project introduces students to API integration, prompt engineering, and AI-powered text summarization.

---

# Learning Objectives

By completing this exercise, students will learn to:

- Work with external Python libraries
- Extract transcripts from YouTube videos
- Build prompts dynamically
- Call the Groq API
- Process and display AI-generated responses
- Handle exceptions gracefully

---

# Problem Statement

Create a Python application that performs the following tasks:

1. Ask the user to enter a YouTube video URL.
2. Extract the Video ID from the URL.
3. Download the transcript of the video.
4. Send the transcript to the Groq LLM.
5. Generate a structured summary.
6. Display the results neatly on the console.

---

# Functional Requirements

The application should generate the following information:

- Video Title (Optional)
- Short Summary (150–200 words)
- Five Key Points
- Three Important Takeaways
- Important Keywords
- Target Audience
- Estimated Difficulty Level
- Suggested Next Steps for Learning

---

# Input

The application should prompt the user as follows:

```text
Enter YouTube Video URL:
```

Example

```text
Enter YouTube Video URL:
https://www.youtube.com/watch?v=xxxxxxxxxxx
```

---

# Expected Output

```text
=========================================================
AI YOUTUBE VIDEO SUMMARY
=========================================================

Video Title
-----------
Introduction to Machine Learning

Summary
-------
This video introduces the basic concepts of machine learning,
including supervised learning, unsupervised learning, datasets,
training, testing, and model evaluation.

Key Points
----------
• What is Machine Learning?
• Types of Machine Learning
• Training vs Testing Data
• Popular Algorithms
• Real-world Applications

Takeaways
----------
1. Machine Learning enables computers to learn from data.
2. Data quality significantly impacts model performance.
3. Practice is essential for mastering ML concepts.

Keywords
---------
Machine Learning
Supervised Learning
Neural Networks
Classification
Regression

Difficulty
----------
Beginner

Target Audience
---------------
Students and software developers interested in AI.

Next Steps
----------
• Learn Python basics
• Study NumPy and Pandas
• Explore Scikit-learn
```

---

# Suggested Prompt

Use an LLM prompt similar to the following:

```text
You are an expert technical educator.

Summarize the following YouTube transcript.

Provide:

1. Summary (150–200 words)
2. Five key points
3. Three important takeaways
4. Important keywords
5. Target audience
6. Difficulty level
7. Suggested next learning steps

Write in simple, clear English.

Format the response using headings and bullet points.
```

---

# Suggested Folder Structure

```text
youtube-video-summarizer/
│
├── main.py
├── groq-api.key
├── requirements.txt
├── README.md
└── output/
```

---

# Recommended Python Packages

```bash
pip install groq
pip install youtube-transcript-api
pip install pytube
```

---

# Suggested Workflow

```
User
   │
   ▼
Enter YouTube URL
   │
   ▼
Extract Video ID
   │
   ▼
Download Transcript
   │
   ▼
Build Prompt
   │
   ▼
Send Transcript to Groq
   │
   ▼
Receive AI Summary
   │
   ▼
Display Results
```

---

# Expected Skills

Students should demonstrate the ability to:

- Read user input
- Parse YouTube URLs
- Use third-party Python libraries
- Build prompts dynamically
- Call the Groq API
- Format AI-generated output
- Handle errors such as invalid URLs or missing transcripts

---

# Bonus Challenges

Enhance the application by adding one or more of the following features:

- Display the video title automatically.
- Translate the summary into another language.
- Generate interview questions from the video.
- Generate quiz questions with answers.
- Perform sentiment analysis on the transcript.
- Export the summary to Markdown.
- Export the summary to PDF.
- Save the summary as a text file.
- Create PowerPoint slides from the summary.
- Ask follow-up questions about the video using the transcript as context.

---

# Deliverables

Students should submit:

- `main.py`
- `requirements.txt`
- `README.md`
- Screenshot of successful execution
- Sample generated summary

---

# Evaluation Criteria

| Criteria | Marks |
|-----------|------:|
| Transcript extraction | 20 |
| Groq API integration | 20 |
| Prompt engineering | 20 |
| Output formatting | 15 |
| Error handling | 10 |
| Code quality | 15 |

**Total:** **100 Marks**

---

# Outcome

At the end of this exercise, students will have built a practical AI application that integrates Python, YouTube transcript extraction, prompt engineering, and Groq-powered Large Language Models to automatically summarize educational videos and extract actionable insights.