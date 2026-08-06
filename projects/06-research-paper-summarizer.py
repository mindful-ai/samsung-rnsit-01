"""
AI Research Paper Summarizer

Requirements

pip install groq
pip install pymupdf
pip install requests
pip install beautifulsoup4
"""

import fitz
import requests
from bs4 import BeautifulSoup
from groq import Groq

# ----------------------------------------------------
# Load API Key
# ----------------------------------------------------

KEY_PATH = r"samsung-ai\key-vault\groq-api.key"

with open(KEY_PATH) as f:
    api_key = f.read().strip()

client = Groq(api_key=api_key)

# ----------------------------------------------------
# Read PDF
# ----------------------------------------------------

def read_pdf(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()

    return text


# ----------------------------------------------------
# Read PubMed Abstract
# ----------------------------------------------------

def read_pubmed(url):

    html = requests.get(url).text

    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("h1")

    if title:
        title = title.text.strip()
    else:
        title = "Unknown"

    abstract = ""

    sections = soup.find_all("div", class_="abstract-content")

    for section in sections:
        abstract += section.get_text(separator=" ", strip=True)

    return f"Title: {title}\n\nAbstract:\n{abstract}"


# ----------------------------------------------------
# Summarize
# ----------------------------------------------------

def summarize(text):

    prompt = f"""
You are an experienced research scientist.

Analyze the following research paper.

Provide

1. Paper Title
2. Authors (if available)
3. Research Domain
4. Research Objective
5. Methodology
6. Dataset Used
7. Key Findings
8. Advantages
9. Limitations
10. Future Work
11. Practical Applications
12. Explain Like I'm 15
13. Overall Summary

Paper

{text[:12000]}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content


# ----------------------------------------------------
# Main
# ----------------------------------------------------

print("=" * 60)
print("AI RESEARCH PAPER SUMMARIZER")
print("=" * 60)

print("\nChoose Input")

print("1. PDF File")
print("2. PubMed URL")

choice = input("\nChoice: ")

if choice == "1":

    pdf = input("PDF Path: ")

    paper_text = read_pdf(pdf)

elif choice == "2":

    url = input("PubMed URL: ")

    paper_text = read_pubmed(url)

else:

    print("Invalid Choice")

    exit()

print("\nSummarizing...\n")

summary = summarize(paper_text)

print("=" * 70)
print(summary)