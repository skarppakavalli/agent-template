
import fitz

from langchain_core.documents import Document


def load_pdf(file_path: str) -> list[Document]:

    documents = []

    # Open PDF using PyMuPDF
    pdf = fitz.open(file_path)

    for page_number, page in enumerate(pdf):

        text = page.get_text()

        # Skip empty pages
        if not text.strip():
            continue

        # Store text and metadata together
        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": file_path,
                    "page": page_number + 1
                }
            )
        )

    return documents
