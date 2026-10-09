
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

from backend.services.ingestion_service import load_documents
from backend.services.chunking_service import chunk_documents

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CHROMA_DIR = PROJECT_ROOT / "data" / "processed" / "chroma_db"
COLLECTION_NAME = "portfolio_knowledge"
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"


def build_vector_store() -> None:
    """Chunk documents, embed them, and persist them in ChromaDB."""

    documents = load_documents()
    chunks = chunk_documents(documents)

    if not chunks:
        raise ValueError("No document chunks found.")

    print(f"Loaded {len(documents)} documents.")
    print(f"Created {len(chunks)} chunks.")
    print("Loading embedding model...")

    model = SentenceTransformer(EMBEDDING_MODEL)

    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    # Rebuild this collection each time to avoid duplicate/stale chunks.
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    batch_size = 64

    for start in range(0, len(chunks), batch_size):
        batch = chunks[start : start + batch_size]

        texts = [chunk["content"] for chunk in batch]
        embeddings = model.encode(
            texts,
            normalize_embeddings=True,
        ).tolist()

        collection.add(
            ids=[chunk["chunk_id"] for chunk in batch],
            documents=texts,
            embeddings=embeddings,
            metadatas=[
                {
                    key: value
                    for key, value in chunk["metadata"].items()
                    if value is not None
                }
                for chunk in batch
            ],
        )

        print(f"Stored {min(start + batch_size, len(chunks))}/{len(chunks)} chunks.")

    print("\nVector database created successfully.")
    print("Collection:", COLLECTION_NAME)
    print("Stored chunks:", collection.count())
    print("Database path:", CHROMA_DIR)


if __name__ == "__main__":
    build_vector_store()