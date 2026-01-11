# Import dataclass decorator to easily define data containers
from dataclasses import dataclass

# Import typing helpers for optional fields and lists
from typing import Optional, List


# Dataclass to represent an uploaded image internally
@dataclass
class ImageInput:
    # Original filename of the image
    filename: str
    # Raw bytes of the image file
    content: bytes
    # MIME type (e.g., image/png, image/jpeg)
    mime_type: str


# Dataclass to represent an uploaded document internally
@dataclass
class DocumentInput:
    # Original filename of the document
    filename: str
    # Raw bytes of the document file
    content: bytes
    # MIME type (e.g., application/pdf)
    mime_type: str


# Dataclass that represents all raw inputs to the pipeline
@dataclass
class RawInput:
    # Optional free-form text input from the user
    text: Optional[str]
    # List of uploaded images (can be empty)
    images: List[ImageInput]
    # List of uploaded documents (can be empty)
    documents: List[DocumentInput]
