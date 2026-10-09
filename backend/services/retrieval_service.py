
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CHROMA_DIR = PROJECT_ROOT / "data" / "processed" / "chroma_db"

COLLECTION_NAME = "portfolio_knowledge"
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

_model = None
_collection = None


def get_model():
    """Load the embedding model once per process."""
    global _model

    if _model is None:
        _model = SentenceTransformer(EMBEDDING_MODEL)

    return _model


def get_collection():
    """Connect to the persistent ChromaDB collection."""
    global _collection

    if _collection is None:
        client = chromadb.PersistentClient(path=str(CHROMA_DIR))
        _collection = client.get_collection(COLLECTION_NAME)

    return _collection


def search_knowledge_base(
    question: str,
    top_k: int = 4,
) -> list[dict]:
    """Retrieve the most relevant document chunks for a question."""

    if not question.strip():
        return []

    collection = get_collection()

    if collection.count() == 0:
        return []

    model = get_model()
    query_embedding = model.encode(
        [f"Represent this sentence for searching relevant passages: {question}"],
        normalize_embeddings=True,
    ).tolist()[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(top_k, collection.count()),
        include=["documents", "metadatas", "distances"],
    )

    matches = []

    for i, content in enumerate(results["documents"][0]):
        matches.append(
            {
                "content": content,
                "metadata": results["metadatas"][0][i],
                "distance": results["distances"][0][i],
            }
        )

    return matches


if __name__ == "__main__":
    question = input("Ask a question about your portfolio: ")
    results = search_knowledge_base(question)

    if not results:
        print("No relevant information found.")
    else:
        for index, result in enumerate(results, start=1):
            print(f"\n--- Result {index} ---")
            print("Title:", result["metadata"].get("title"))
            print("Source:", result["metadata"].get("source_name"))
            print("Distance:", round(result["distance"], 4))
            print("Content:", result["content"][:500])