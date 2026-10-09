
from backend.connectors.docling_connector import extract_pdf
from backend.connectors.text_connector import extract_markdown

# Change these paths to files that actually exist on your computer.
pdf_document = extract_pdf("data/raw/profile.pdf")

markdown_document = extract_markdown(
    "data/raw/projects/youtube_qna.md"
)

for document in [pdf_document, markdown_document]:
    print("\n--- Extracted document ---")
    print("ID:", document.document_id)
    print("Title:", document.title)
    print("Type:", document.source_type)
    print("Content preview:", document.content[:300])
    print("Metadata:", document.metadata)