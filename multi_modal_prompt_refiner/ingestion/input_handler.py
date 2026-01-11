# Import typing helpers
from typing import Optional, List

# Import internal data structures
from normalization.semantic_schema import RawInput, ImageInput, DocumentInput


def build_raw_input(
    text: Optional[str],
    images: Optional[List],
    documents: Optional[List]
) -> RawInput:
    """
    Converts raw UI / CLI inputs into a normalized RawInput object.
    """

    # Initialize an empty list to store processed images
    image_inputs: List[ImageInput] = []

    # If image files were provided
    if images:
        # Loop through each uploaded image
        for img in images:
            # Create an ImageInput object from uploaded file
            image_inputs.append(
                ImageInput(
                    filename=img.name,          # Store original filename
                    content=img.read(),          # Read raw bytes
                    mime_type=img.type           # Store MIME type
                )
            )

    # Initialize an empty list to store processed documents
    document_inputs: List[DocumentInput] = []

    # If document files were provided
    if documents:
        # Loop through each uploaded document
        for doc in documents:
            # Create a DocumentInput object from uploaded file
            document_inputs.append(
                DocumentInput(
                    filename=doc.name,           # Store original filename
                    content=doc.read(),           # Read raw bytes
                    mime_type=doc.type            # Store MIME type
                )
            )

    # Create and return the unified RawInput object
    return RawInput(
        text=text if text else None,   # Normalize empty text to None
        images=image_inputs,            # Always a list (possibly empty)
        documents=document_inputs       # Always a list (possibly empty)
    )
