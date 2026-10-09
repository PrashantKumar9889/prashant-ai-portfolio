
from pathlib import Path

from docling.document_converter import DocumentConverter

from backend.schemas.document import SourceDocument


# Initialize once per process, not once per document.
_converter = DocumentConverter()


def extract_pdf(
    file_path: str,
    source_url: str | None = None,
) -> SourceDocument:
    """Extract a PDF and return a normalized SourceDocument."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")

    result = _converter.convert(str(path))
    content = result.document.export_to_markdown()

    if not content.strip():
        raise ValueError(f"No text extracted from PDF: {path}")

    return SourceDocument(
        document_id=f"pdf-{path.stem}",
        title=path.stem.replace("_", " ").replace("-", " ").title(),
        content=content,
        source_type="pdf",
        source_name=path.name,
        source_url=source_url,
        metadata={
            "file_name": path.name,
            "file_path": str(path.resolve()),
        },
    )