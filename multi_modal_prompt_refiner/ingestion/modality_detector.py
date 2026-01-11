# Import the RawInput structure
from normalization.semantic_schema import RawInput


def detect_modalities(raw_input: RawInput) -> dict:
    """
    Detects which input modalities are present in the RawInput.
    """

    # Determine if text is present
    has_text = raw_input.text is not None and raw_input.text.strip() != ""

    # Determine if at least one image is present
    has_images = len(raw_input.images) > 0

    # Determine if at least one document is present
    has_documents = len(raw_input.documents) > 0

    # Return modality presence flags
    return {
        "has_text": has_text,
        "has_images": has_images,
        "has_documents": has_documents
    }




