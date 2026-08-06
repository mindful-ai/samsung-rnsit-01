"""
AI Image Processor

pip install groq pillow rich

Set GROQ_API_KEY
"""

import json
import os

from groq import Groq

from PIL import Image
from PIL import ImageEnhance
from rich.console import Console

console = Console()

SYSTEM_PROMPT = """
You are an image processing assistant.

Convert the user's request into JSON.

Supported operations:

brightness
contrast
sharpness
color
rotate
grayscale
flip_horizontal
flip_vertical

Return ONLY JSON.

Schema

{
 "operations":[
   {
      "operation":"",
      "value":0
   }
 ]
}
"""

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

image_path = console.input(
    "[cyan]Image Path:[/cyan] "
)

instruction = console.input(
    "[cyan]Editing Instruction:[/cyan] "
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    response_format={"type":"json_object"},
    messages=[
        {
            "role":"system",
            "content":SYSTEM_PROMPT
        },
        {
            "role":"user",
            "content":instruction
        }
    ]
)

operations = json.loads(
    response.choices[0].message.content
)

img = Image.open(image_path)

for op in operations["operations"]:

    if op["operation"] == "brightness":
        img = ImageEnhance.Brightness(img).enhance(op["value"])

    elif op["operation"] == "contrast":
        img = ImageEnhance.Contrast(img).enhance(op["value"])

    elif op["operation"] == "sharpness":
        img = ImageEnhance.Sharpness(img).enhance(op["value"])

    elif op["operation"] == "color":
        img = ImageEnhance.Color(img).enhance(op["value"])

    elif op["operation"] == "rotate":
        img = img.rotate(op["value"])

    elif op["operation"] == "grayscale":
        img = img.convert("L")

    elif op["operation"] == "flip_horizontal":
        img = img.transpose(Image.FLIP_LEFT_RIGHT)

    elif op["operation"] == "flip_vertical":
        img = img.transpose(Image.FLIP_TOP_BOTTOM)

output = "output.jpg"

img.save(output)

console.print(
    f"[green]Image saved as {output}[/green]"
)