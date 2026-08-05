# Good Prompt vs Bad Prompt

These short examples demonstrate how adding context and requirements improves AI responses.

---

# Example 1: Code Generation

## ❌ Bad Prompt

```text
Write a Python program.
```

**Why it's bad:** No objective, requirements, or expected output.

## ✅ Good Prompt

```text
You are a Python developer.

Write a Python program to read a CSV file of employee salaries, calculate the average salary by department, and save the results to a new CSV. Use pandas and include comments.
```

---

# Example 2: Image Generation

## ❌ Bad Prompt

```text
Draw a cat.
```

## ✅ Good Prompt

```text
Create a photorealistic image of a white Persian cat sitting on a wooden windowsill during golden hour, with soft natural lighting, shallow depth of field, and no text or watermark.
```

---

# Example 3: Video Generation

## ❌ Bad Prompt

```text
Make a robot video.
```

## ✅ Good Prompt

```text
Create a 10-second cinematic video of a humanoid robot walking through a futuristic neon-lit city at night. Use a slow tracking camera, realistic lighting, and 4K quality.
```

---

# Example 4: Explanation

## ❌ Bad Prompt

```text
Explain AI.
```

## ✅ Good Prompt

```text
Explain Generative AI to a first-year engineering student using simple language, everyday examples, and no mathematical equations. Limit the explanation to 200 words.
```

---

# Rule of Thumb

**Bad Prompt**

```text
What
```

Example:

```text
Write Python code.
```

**Good Prompt**

```text
Role + Task + Constraints + Expected Output
```

Example:

```text
You are a Python developer. Write a Python program to process a CSV using pandas, include comments, handle missing values, and explain the solution.
```
