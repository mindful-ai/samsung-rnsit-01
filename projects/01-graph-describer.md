# AI Graph Analyzer

## Classroom Exercise

**Duration:** 60 Minutes

**Difficulty:** Beginner

**Programming Language:** Python

**LLM:** Groq

---

# Objective

Graphs and charts are commonly used to communicate information. Understanding them quickly is an important skill.

Develop an **AI Graph Analyzer** that accepts an image of a graph and uses a Large Language Model (LLM) to describe and analyze it.

The application should identify the graph type, interpret the data, summarize important observations, and generate meaningful insights.

---

# Learning Objectives

By completing this exercise, students will learn to:

- Read image files using Python
- Use multimodal Large Language Models
- Build effective prompts
- Integrate the Groq API
- Process AI-generated responses
- Build a real-world AI application

---

# Problem Statement

Create a Python application that performs the following steps:

1. Ask the user to enter the path of a graph image.
2. Read the image from disk.
3. Send the image to the Groq multimodal model.
4. Receive the AI-generated analysis.
5. Display the results in a structured format.

---

# Functional Requirements

The application should identify:

- Graph type
- Graph title
- X-axis label
- Y-axis label
- Units (if available)
- Categories or legends
- Highest value
- Lowest value
- Maximum trend
- Minimum trend

The application should also generate:

- Five important observations
- Three business insights
- Three recommendations
- A concise summary (100–150 words)

---

# Supported Graph Types

The application should work with common chart types such as:

- Bar Chart
- Line Chart
- Pie Chart
- Scatter Plot
- Histogram
- Area Chart
- Stacked Bar Chart
- Box Plot (Bonus)

---

# Input

The application should prompt the user as follows:

```text
Enter graph image path:
```

Example

```text
Enter graph image path:
sales_chart.png
```

---

# Expected Output

```text
=========================================================
AI GRAPH ANALYSIS
=========================================================

Graph Type
----------
Bar Chart

Title
-----
Quarterly Sales

X-Axis
------
Quarter

Y-Axis
------
Revenue (₹ Lakhs)

Highest Value
-------------
Q4 : ₹82 Lakhs

Lowest Value
------------
Q1 : ₹35 Lakhs

Key Observations
----------------
• Revenue increases every quarter.
• Q4 has the highest revenue.
• No declining trend is observed.
• Sales growth accelerates during the last quarter.
• Revenue nearly doubles over the year.

Business Insights
-----------------
• Demand is increasing steadily.
• Marketing campaigns appear effective.
• Production capacity may need expansion.

Recommendations
---------------
• Increase inventory for Q4.
• Allocate higher marketing budget.
• Monitor supply chain for increased demand.

Summary
-------
The graph indicates consistent business growth throughout the year with
strong performance in the final quarter. The trend suggests increasing
customer demand and healthy revenue growth.
```

---

# Suggested Prompt

Use an LLM prompt similar to the following:

```text
You are an expert data analyst.

Analyze the graph image and provide:

1. Graph type
2. Graph title
3. X-axis label
4. Y-axis label
5. Units
6. Highest value
7. Lowest value
8. Five important observations
9. Three business insights
10. Three recommendations
11. Overall summary

If any information is missing, state "Not Available."

Format the response neatly using headings and bullet points.
```

---

# Suggested Folder Structure

```text
graph-analyzer/
│
├── main.py
├── graph.png
├── groq-api.key
├── requirements.txt
└── README.md
```

---

# Recommended Python Packages

```bash
pip install groq
pip install pillow
```

---

# Expected Skills

Students should demonstrate the ability to:

- Read image files
- Encode images for API requests
- Construct prompts
- Invoke the Groq API
- Display formatted output
- Handle invalid file paths gracefully

---

# Bonus Challenges

Enhance the application by adding one or more of the following features:

- Support multiple graph images.
- Compare two graphs.
- Export the analysis to a Markdown file.
- Export the analysis to PDF.
- Generate PowerPoint slides from the analysis.
- Translate the analysis into another language.
- Answer follow-up questions about the graph using the LLM.
- Estimate future trends based on the graph.
- Provide business recommendations tailored to the detected trends.

---

# Deliverables

Students should submit:

- Python source code (`main.py`)
- `requirements.txt`
- Sample graph images
- Screenshot of program execution
- Generated graph analysis

---

# Evaluation Criteria

| Criteria | Marks |
|-----------|------:|
| Reads image successfully | 10 |
| Calls Groq API correctly | 20 |
| Prompt design | 20 |
| Output formatting | 15 |
| Error handling | 10 |
| Code quality | 15 |
| Bonus features | 10 |

**Total:** **100 Marks**

---

# Outcome

At the end of this exercise, students will have built a practical multimodal AI application that combines Python programming, image processing, prompt engineering, and Groq-powered Large Language Models to automatically understand and explain graphical data.