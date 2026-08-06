# 3. Advanced Prompting Techniques

## 3.1 Zero-Shot & Few-Shot Prompting, System Prompts & Instructions

### Zero-Shot Prompting

The AI is given only the task without any examples.

**Use when**
- The task is simple.
- The model already has sufficient knowledge.
- You need a quick response.

**Example**

```text
Summarize the following article in 100 words.
```

**Advantage:** Fast and simple.

**Limitation:** Output style and quality may vary.

---

### Few-Shot Prompting

Provide one or more examples before asking the AI to perform the task.

**Use when**
- Consistent output is required.
- The task follows a specific pattern.
- You want to teach the desired format.

**Example**

```text
Example

Input:
Apple

Output:
Fruit

Input:
Carrot

Output:
Vegetable

Input:
Salmon

Output:
?
```

**Expected Output**

```text
Fish
```

**Advantage:** Improves consistency and accuracy.

---

### System Prompts

A system prompt defines the AI's overall behavior throughout the conversation.

**Example**

```text
You are an experienced AI instructor.
Explain concepts using simple language and practical examples.
```

**Purpose:** Sets the AI's role, tone, and behavior.

---

### Instructions

Instructions specify what the AI should do for a particular task.

**Example**

```text
Summarize the document in bullet points.
Limit the response to 150 words.
```

**Difference**
- System Prompt: Defines overall behavior.
- Instruction: Defines the current task.

---

## 3.2 Style Control, Schema-First Prompting & Template Reuse

### Style Control

Specify how the response should be written.

**Example**

```text
Explain Generative AI.

Style: Professional
Audience: Business Executives
Tone: Concise
```

Common styles:
- Technical
- Beginner-friendly
- Academic
- Conversational
- Executive Summary

---

### Schema-First Prompting

Define the expected output structure before asking the question.

**Example**

```text
Return JSON using this schema:

{
  "name": "",
  "department": "",
  "experience": 0,
  "skills": []
}
```

**Benefits**
- Machine-readable output
- Easy API integration
- Reliable automation

---

### Template Reuse

Create reusable prompt templates for repetitive tasks.

**Template**

```text
Role:
<role>

Task:
<task>

Context:
<context>

Constraints:
<constraints>

Output:
<format>
```

**Example**

```text
Role:
Data Analyst

Task:
Analyze monthly sales

Context:
Retail sales dataset

Constraints:
Maximum 200 words

Output:
Executive summary with recommendations
```

**Benefits**
- Consistent prompts
- Faster development
- Standardized AI interactions

---

# Key Takeaways

| Technique | Purpose | Best Use |
|-----------|---------|----------|
| Zero-Shot | Perform a task without examples | Simple tasks |
| Few-Shot | Learn from examples | Consistent outputs |
| System Prompt | Define AI behavior | Entire conversation |
| Instruction | Define the current task | Individual requests |
| Style Control | Control tone and audience | Content generation |
| Schema-First | Specify output structure | APIs, automation, data extraction |
| Template Reuse | Reuse proven prompt patterns | Repetitive workflows |
