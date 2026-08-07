"""
restaurant_rag_chatbot.py

Requirements

pip install groq chromadb sentence-transformers

Set:

GROQ_API_KEY=<your key>

Run:

python restaurant_rag_chatbot.py
"""

import os

from groq import Groq
import chromadb
from chromadb.utils.embedding_functions import (
    SentenceTransformerEmbeddingFunction
)

# --------------------------------------------------------
# Configuration
# --------------------------------------------------------

COLLECTION_NAME = "restaurant_knowledge"

embedding_fn = SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    COLLECTION_NAME,
    embedding_function=embedding_fn
)

groq = Groq(
    api_key=""
)

SYSTEM_PROMPT = """
You are an AI Restaurant Assistant.

Answer ONLY using the retrieved restaurant knowledge.

If the answer cannot be found,
say

"I could not find that information in the restaurant database."

Always be helpful.

When recommending food,

consider

- budget
- number of people
- offers
- combo meals
- reservation policies
- customer reviews

Produce a clear recommendation.
"""

# --------------------------------------------------------

while True:

    question = input("\nQuestion (or exit): ")

    if question.lower() in (
        "exit",
        "quit",
        "stop"
    ):
        break

    results = collection.query(
        query_texts=[question],
        n_results=8
    )

    context = "\n\n".join(
        results["documents"][0]
    )

    prompt = f"""
Restaurant Knowledge

{context}

Customer Question

{question}

Answer using ONLY the above information.
"""

    response = groq.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("\n" + "=" * 60)
    print(response.choices[0].message.content)

    print("\nRetrieved Documents")
    print("-" * 60)

    for i, meta in enumerate(results["metadatas"][0], 1):

        print(
            f"{i}. "
            f"{meta.get('document_type')} | "
            f"{meta.get('title')}"
        )