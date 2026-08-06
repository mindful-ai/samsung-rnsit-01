# Prompt Engineering Demonstration: Vague vs Step-by-Step vs ReAct

# Problem Statement

A university student has **7 days** to complete **8 assignments** before the semester ends.

The student can study **a maximum of 5 hours per day**.

## Resource Constraints

- Laptop: Available every day
- Internet: Available **only on Days 3, 4 and 5**
- AI Lab: Available **only on Day 4**
- Only **one assignment can be worked on at a time**

Some assignments depend on others, require special resources, and have deadlines.

**Objective:** Maximize the total marks earned while meeting all deadlines and constraints.

## Assignment Details

| ID | Assignment | Duration | Marks | Deadline | Prerequisite | Resources Required |
|----|------------|---------:|------:|----------|--------------|--------------------|
| A | Python Basics | 2 hrs | 10 | Day 2 | None | Laptop |
| B | Data Analysis | 3 hrs | 15 | Day 4 | A | Laptop |
| C | Machine Learning Model | 4 hrs | 25 | Day 6 | B | Laptop + Internet |
| D | Power BI Dashboard | 2 hrs | 10 | Day 5 | A | Laptop |
| E | Database Design | 3 hrs | 15 | Day 5 | None | Laptop |
| F | AI Chatbot | 5 hrs | 30 | Day 7 | C and E | Laptop + Internet + AI Lab |
| G | Final Presentation | 2 hrs | 10 | Day 7 | D and F | Laptop |
| H | Project Report | 3 hrs | 20 | Day 7 | B | Laptop |

## Constraints

- Maximum **5 study hours per day**
- Only **one assignment at a time**
- Internet available only on **Days 3–5**
- AI Lab available only on **Day 4**
- All prerequisites must be completed first
- Missing a deadline gives **zero marks**
- Goal: **maximize total marks**

---

# Prompt 1 – Vague Prompt

```text
Create the best study schedule for the above assignments.
```

**Typical Issues**

- May ignore resource constraints.
- May overlook deadlines.
- May violate prerequisites.
- May not maximize marks.
- Provides little justification.

---

# Prompt 2 – Step-by-Step Prompt

```text
You are an aptitude trainer and project planning expert.

Solve the scheduling problem systematically.

Follow these steps:

1. List all prerequisites.
2. Identify all resource constraints.
3. List all deadlines.
4. Calculate the total workload.
5. Identify the critical path.
6. Identify assignments that can be completed independently.
7. Prioritize assignments based on:
   - Prerequisites
   - Deadlines
   - Marks
   - Resource availability
8. Create a day-by-day study schedule.
9. Verify:
   - Daily study hours
   - Resource availability
   - Prerequisites
   - Deadlines
10. Calculate:
    - Total marks earned
    - Assignments completed
    - Any assignments that could not be completed

Present the final schedule in a table.
```

---

# Prompt 3 – ReAct Prompt

```text
You are an experienced project planning expert.

Solve the scheduling problem using a Reason–Evaluate–Revise (ReAct) approach.

Reason:
- Analyze prerequisites.
- Analyze deadlines.
- Analyze resource constraints.
- Identify the critical path.
- Produce an initial schedule.

Evaluate:
Check whether the schedule:
- Violates any prerequisite.
- Exceeds 5 study hours per day.
- Uses Internet only on Days 3–5.
- Uses the AI Lab only on Day 4.
- Misses any deadline.
- Maximizes total marks.

Revise:
If any issue is found, revise the schedule and evaluate again.
Repeat until all constraints are satisfied.

Finally present:

1. Constraint Summary
2. Initial Schedule
3. Evaluation Results
4. Revised Final Schedule
5. Total Marks Earned
6. Final Conclusion

Provide concise reasoning summaries for each phase rather than internal reasoning.
```

---

# Expected Learning Outcome

| Prompt Type | Characteristics | Expected Result |
|-------------|-----------------|-----------------|
| Vague | Simple request | May overlook constraints and produce an incomplete schedule |
| Step-by-Step | Structured analysis and verification | More reliable, organized, and verifiable schedule |
| ReAct | Iterative Reason → Evaluate → Revise workflow | Refined solution that checks and improves itself before presenting the final schedule |
