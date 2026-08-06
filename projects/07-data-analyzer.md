# AI Data Analysis Assistant

## Classroom Exercise

**Duration:** 60 Minutes

**Difficulty:** Beginner

**Programming Language:** Python

**LLM:** Groq

---

# Objective

Data analysts frequently use Pandas to answer questions about datasets. However, writing Pandas code requires programming knowledge.

Develop an **AI Data Analysis Assistant** that allows users to ask questions in natural language and automatically generates and executes the corresponding Pandas operations.

The application should read a CSV dataset and answer user questions without requiring the user to write Python code.

---

# Learning Objectives

By completing this exercise, students will learn to:

- Read CSV datasets using Pandas
- Understand dataframe metadata
- Use Large Language Models for code generation
- Execute generated Python code safely
- Display analysis results
- Build AI-powered data analysis tools

---

# Problem Statement

Create a Python application that performs the following steps:

1. Load a CSV dataset.
2. Display dataset information.
3. Allow the user to ask questions in natural language.
4. Send the dataset schema and user query to the Groq LLM.
5. Generate Pandas code.
6. Execute the generated code.
7. Display the results.

The application should continue until the user types:

```
exit
quit
stop
```

---

# Functional Requirements

The application should support queries such as:

- Show the first 10 rows.
- Show the last 5 rows.
- Display column names.
- Count the number of rows.
- Calculate average salary.
- Find maximum sales.
- Find minimum price.
- Show employees older than 30.
- Sort by salary descending.
- Group by department.
- Show total sales by region.
- Find duplicate records.
- Count missing values.
- Filter rows where City = Bangalore.
- Display summary statistics.
- Calculate correlation.

---

# Sample Input

```
Dataset:
sales.csv

Question:
Show the top 5 products by sales.
```

---

# Sample Output

```
====================================================
Generated Pandas Code
====================================================

df.sort_values(
    by="Sales",
    ascending=False
).head(5)

====================================================
Result
====================================================

Product        Sales

Laptop         980000
Tablet         860000
...
```

---

# Prompt Template

```
You are an expert Python data analyst.

A Pandas dataframe named df has already been loaded.

Columns:

{columns}

Data Types:

{dtypes}

Generate ONLY executable Pandas code.

Rules:

• Return Python code only.
• Do not include markdown.
• Do not include explanations.
• Use dataframe variable df.
• Store the final answer in a variable named result.

User Question:

{question}
```

---

# Suggested Folder Structure

```
data-analysis-assistant/
│
├── main.py
├── sales.csv
├── groq-api.key
├── requirements.txt
└── README.md
```

---

# Recommended Packages

```bash
pip install groq
pip install pandas
```

---

# Expected Skills

Students should demonstrate the ability to

- Read CSV files
- Explore datasets
- Use dataframe metadata
- Generate Pandas code using an LLM
- Execute generated code
- Display formatted output
- Handle runtime errors

---

# Bonus Challenges

Students can extend the application to

- Generate charts automatically
- Export results to CSV
- Save generated code
- Support Excel files
- Create dashboards
- Generate business insights
- Explain the generated code
- Generate SQL equivalent
- Suggest additional analyses

---

# Deliverables

Students should submit

- main.py
- requirements.txt
- sample.csv
- README.md

---

# Evaluation Criteria

| Criteria | Marks |
|----------|------:|
| CSV Loading | 15 |
| Prompt Engineering | 20 |
| Groq API Integration | 20 |
| Pandas Code Generation | 20 |
| Code Execution | 15 |
| Error Handling | 10 |

**Total: 100 Marks**

---

# Outcome

Students will build an AI-powered data analysis assistant capable of translating natural language questions into executable Pandas code, enabling interactive exploration of datasets using Python and Groq.