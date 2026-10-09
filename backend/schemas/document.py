
from datetime import datetime, timezone

from pydantic import BaseModel, Field


class SourceDocument(BaseModel):
    """Standard representation of content from any data source."""

    document_id: str
    title: str
    content: str

    source_type: str
    source_name: str
    source_url: str | None = None

    metadata: dict = Field(default_factory=dict)

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )