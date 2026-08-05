# 2. What is Prompt Engineering?

Prompt engineering is the process of designing clear, structured, and effective instructions (prompts) that guide an AI model to produce accurate, relevant, and useful responses. It involves choosing the right words, providing sufficient context, specifying constraints, and defining the desired output format so that the AI understands exactly what is expected.

A well-crafted prompt reduces ambiguity, improves consistency, minimizes hallucinations, and often eliminates the need for repeated corrections.

## Benefits
- Produces more accurate and relevant responses.
- Reduces ambiguity and misunderstandings.
- Improves consistency across interactions.
- Saves time by reducing prompt iterations.
- Enables AI to perform specialized tasks effectively.

---

# 2.1 Role, Goal, Context, Constraints, Style, Output Format

An effective prompt typically consists of six essential components.

| Component | Purpose | Example |
|-----------|---------|---------|
| **Role** | Defines the AI's expertise or perspective | You are a cybersecurity consultant. |
| **Goal** | Specifies the task to accomplish | Prepare a security awareness plan. |
| **Context** | Provides background information | The organization has 500 employees. |
| **Constraints** | Defines limitations or rules | Limit to 500 words. Use ISO 27001. |
| **Style** | Specifies tone and writing style | Professional and concise. |
| **Output Format** | Defines how the response should be presented | Markdown table followed by recommendations. |

### Example Prompt

```text
Role:
You are a senior data analyst.

Goal:
Analyze monthly sales performance.

Context:
The dataset contains sales data from 12 regions.

Constraints:
Use only the supplied data.
Limit the summary to 300 words.

Style:
Professional and concise.

Output Format:
1. Executive Summary
2. Sales Table
3. Key Insights
4. Recommendations
```

---

# 2.2 Learning Domain Context, Negative Prompting, and Verification Techniques

## Learning Domain Context

Specify the target audience so the AI adjusts the explanation.

### Examples

```text
Explain Kubernetes to a beginner software developer.
```

```text
Explain machine learning to a high school student.
```

## Negative Prompting

Tell the AI what to avoid.

### Examples

```text
Do not use technical jargon.
Do not invent facts.
Do not include marketing language.
Avoid unnecessary explanations.
```

## Verification Techniques

Ask the AI to validate its own response.

### Example

```text
After generating the answer:

- Verify factual consistency.
- Highlight assumptions made.
- Identify limitations.
- Mention areas that require human verification.
```

---

# 2.3 Designing Structured and Verifiable Outputs

Structured outputs are easier to review, validate, automate, and integrate.

## Example – Structured Response

```text
Explain cloud computing.

Return:
1. Definition
2. Advantages
3. Disadvantages
4. Real-world Examples
5. Summary
```

## Example – Markdown Table

```text
Compare AWS, Azure, and Google Cloud.

Output:
- Provider
- Strengths
- Weaknesses
- Best Use Cases
```

## Example – JSON

```json
{
  "name": "",
  "department": "",
  "experience": "",
  "skills": []
}
```

## Best Practices

- Request numbered sections or tables.
- Specify the exact output format (Markdown, JSON, CSV, XML, YAML).
- Separate facts from assumptions.
- Ask for citations when appropriate.
- Request a final self-review.
- Define acceptance criteria.

---

# Key Takeaways

- **Role** defines who the AI should be.
- **Goal** defines the objective.
- **Context** provides background.
- **Constraints** define boundaries.
- **Style** controls tone.
- **Output Format** structures the response.
- **Negative prompting** reduces unwanted output.
- **Verification** improves reliability.
- **Structured outputs** simplify validation and automation.
