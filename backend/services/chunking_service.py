
from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.schemas.document import SourceDocument


def chunk_documents(
    documents: list[SourceDocument],
    chunk_size: int = 800,
    chunk_overlap: int = 120,
) -> list[dict]:
    """Split documents into overlapping chunks while preserving source metadata."""

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        add_start_index=True,
    )

    chunks = []

    for document in documents:
        text_chunks = splitter.create_documents(
            texts=[document.content],
            metadatas=[
                {
                    "document_id": document.document_id,
                    "title": document.title,
                    "source_type": document.source_type,
                    "source_name": document.source_name,
                    "source_url": document.source_url or "",
                }
            ],
        )

        for index, chunk in enumerate(text_chunks):
            chunks.append(
                {
                    "chunk_id": f"{document.document_id}-chunk-{index}",
                    "content": chunk.page_content,
                    "metadata": chunk.metadata,
                }
            )

    return chunks


if __name__ == "__main__":
    from backend.services.ingestion_service import load_documents

    documents = load_documents()
    chunks = chunk_documents(documents)

    print(f"Documents loaded: {len(documents)}")
    print(f"Chunks created: {len(chunks)}")

    for chunk in chunks[:3]:
        print("\n" + "-" * 50)
        print("Chunk ID:", chunk["chunk_id"])
        print("Metadata:", chunk["metadata"])
        print("Content preview:", chunk["content"][:200])