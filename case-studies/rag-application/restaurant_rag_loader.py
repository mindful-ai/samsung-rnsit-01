"""
restaurant_rag_loader.py

Load the restaurant_rag_dataset_500.csv into ChromaDB.

Install:
    pip install chromadb pandas sentence-transformers

Run:
    python restaurant_rag_loader.py
"""

import json
import pandas as pd
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

CSV_FILE = "restaurant_rag_dataset_500.csv"
COLLECTION_NAME = "restaurant_knowledge"

df = pd.read_csv(CSV_FILE)

client = chromadb.PersistentClient(path="./chroma_db")

embedding_fn = SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_fn
)

ids = []
documents = []
metadatas = []

for _, row in df.iterrows():
    ids.append(str(row["document_id"]))
    documents.append(str(row["content"]))

    meta = {
        "document_type": row["document_type"],
        "title": row["title"],
        "category": row["category"],
        "tags": row["tags"],
    }

    try:
        extra = json.loads(row["metadata"]) if pd.notna(row["metadata"]) else {}
        if isinstance(extra, dict):
            meta.update(extra)
    except Exception:
        pass

    metadatas.append(meta)

BATCH = 100

for i in range(0, len(ids), BATCH):
    collection.add(
        ids=ids[i:i+BATCH],
        documents=documents[i:i+BATCH],
        metadatas=metadatas[i:i+BATCH]
    )
    print(f"Loaded {min(i+BATCH, len(ids))} / {len(ids)} documents")

print("\nDone!")
print("Collection :", COLLECTION_NAME)
print("Documents  :", collection.count())

print("\nExample query:\n")

results = collection.query(
    query_texts=[
        "Happy hour offers for four people under 1000 rupees"
    ],
    n_results=5
)

for i, doc in enumerate(results["documents"][0], start=1):
    print("-"*60)
    print(f"Result {i}")
    print(doc)
    print(results["metadatas"][0][i-1])
