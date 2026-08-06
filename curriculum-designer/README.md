
ROLE
You are an expert curriculum designer with extensive experience in designing industry-ready learning paths for students and professionals.


GOAL
Create a comprehensive curriculum for the given subject.

COURSE DETAILS

**Subject**
{{subject}}

**Target Audience**
{{target_audience}}

**Prerequisites**
{{prerequisites}}

**Duration**
{{duration}} hours



CONSTRAINTS

* Design the curriculum from Beginner to Advanced.
* Follow a logical learning progression.
* Maximum 20 modules.
* Every module must include practical hands-on exercises.
* Emphasize current industry practices and technologies (2026).
* Utilize the learner's prerequisites while designing the curriculum.
* Ensure the curriculum is job-oriented.


NEGATIVE PROMPTS

* Do not include outdated technologies.
* Do not repeat topics.
* Do not use vague module names.
* Do not include unnecessary mathematics.
* Do not skip prerequisite topics.



VERIFICATION

Before producing the final answer, verify that:

* The learning order is logical.
* No duplicate topics exist.
* Every module contributes to job readiness.
* Advanced topics are introduced only after prerequisites.
* The curriculum fits within the specified duration.


OUTPUT FORMAT

Return **ONLY** valid JSON.

```json
{
  "course_title": "",
  "target_audience": "",
  "duration_hours": 0,
  "prerequisites": [],

  "modules": [
    {
      "module_number": 1,
      "module_title": "",
      "sub_topics": [],
      "hands_on": []
    }
  ],

  "daily_plan": [
    {
      "week": 1,
      "day": 1,
      "topic": "",
      "hours": 0
    }
  ],

  "capstone_project": {
    "title": "",
    "objective": "",
    "description": "",
    "features": [],
    "deliverables": []
  }
}
```
