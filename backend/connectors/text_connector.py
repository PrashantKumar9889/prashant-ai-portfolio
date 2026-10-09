
from pathlib import Path

from backend.schemas.document import SourceDocument


def extract_markdown(
    file_path: str,
    source_url: str | None = None,
) -> SourceDocument:
    """Read Markdown and normalize it into a SourceDocument."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Markdown file not found: {path}")

    content = path.read_text(encoding="utf-8")

    if not content.strip():
        raise ValueError(f"Markdown file is empty: {path}")

    return SourceDocument(
        document_id=f"markdown-{path.stem}",
        title=path.stem.replace("_", " ").replace("-", " ").title(),
        content=content,
        source_type="markdown",
        source_name=path.name,
        source_url=source_url,
        metadata={
            "file_name": path.name,
            "file_path": str(path.resolve()),
        },
    )