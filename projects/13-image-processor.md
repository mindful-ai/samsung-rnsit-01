# Project: AI Image Processor

## Objective

Develop an AI-powered Image Processor that accepts image editing instructions in natural language and automatically applies them to an image.

The application should use an LLM to convert natural language into structured image processing commands.

---

# Problem Statement

Build a Python application that accepts:

- An input image
- Natural language editing instructions

The AI should interpret the user's request and return a structured JSON response.

Python should then apply the requested image transformations and save the edited image.

---

# Functional Requirements

The application shall:

1. Load an image.
2. Accept natural language instructions.
3. Use Groq to interpret the instructions.
4. Return image editing operations as JSON.
5. Apply the operations.
6. Save the processed image.

---

# Supported Operations

- Brightness
- Contrast
- Sharpness
- Color Saturation
- Blur
- Rotate
- Flip Horizontal
- Flip Vertical
- Grayscale
- Resize

Multiple operations may be requested in one sentence.

---

# Example Inputs

Increase brightness by 20%.

Reduce contrast by 10%.

Rotate image by 90 degrees.

Increase brightness by 10% and reduce contrast by 5%.

Convert to grayscale.

Resize to 800 x 600.

Rotate by 180 degrees and increase sharpness by 15%.

---

# Example Output

```json
{
    "operations":[
        {
            "operation":"brightness",
            "value":1.10
        },
        {
            "operation":"contrast",
            "value":0.95
        }
    ]
}
```

---

# JSON Schema

```json
{
    "operations":[
        {
            "operation":"",
            "value":0
        }
    ]
}
```

---

# Technical Requirements

- Python
- Groq API
- Pillow (PIL)
- JSON Output
- Rich Console

---

# Future Enhancements

- Crop
- Background Removal
- Face Enhancement
- Object Detection
- OCR
- Image Captioning
- Streamlit UI