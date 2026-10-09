
from pathlib import Path

from backend.connectors.docling_connector import extract_pdf
from backend.connectors.text_connector import extract_markdown
from backend.schemas.document import SourceDocument

# Project root: Portfolio Website/
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "raw"


def load_documents() -> list[SourceDocument]:
    """Load supported local files into a normalized document collection."""

    documents: list[SourceDocument] = []

    # Load PDF files recursively.
    for pdf_path in DATA_DIR.rglob("*.pdf"):
        document = extract_pdf(str(pdf_path))
        documents.append(document)

    # Load Markdown files recursively.
    for md_path in DATA_DIR.rglob("*.md"):
        document = extract_markdown(str(md_path))
        documents.append(document)

    return documents


if __name__ == "__main__":
    documents = load_documents()

    print(f"\nTotal documents loaded: {len(documents)}")

    for document in documents:
        print("-" * 50)
        print("ID:", document.document_id)
        print("Title:", document.title)
        print("Type:", document.source_type)
        print("Characters:", len(document.content))