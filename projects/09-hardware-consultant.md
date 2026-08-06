# Project: Mobile and Computer Configuration Suggestor System

## Objective
Build an AI assistant that recommends suitable mobile phones or computer configurations based on a user's requirements and budget.

## Problem Statement
Create a Python application that accepts natural language input and recommends an appropriate mobile phone, laptop, or desktop configuration.

### Inputs
- Device Type (Mobile/Laptop/Desktop)
- Budget
- Primary Use (Programming, Gaming, AI/ML, Office, Student, Video Editing, General)
- Preferred Operating System
- Preferred Brand (Optional)

### Outputs
- Recommended Configuration
- Suggested Models
- Price Range
- Justification

## Functional Requirements
1. Accept user requirements.
2. Use an LLM (Groq) to understand the request.
3. Return recommendations in JSON.
4. Display results in a formatted table.

## JSON Schema

```json
{
  "device_type":"",
  "recommended_configuration":{
    "processor":"",
    "ram":"",
    "storage":"",
    "gpu":"",
    "display":"",
    "battery":""
  },
  "price_range":"",
  "recommended_models":[],
  "reason":""
}
```
