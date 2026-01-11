# Import RawInput structure
from normalization.semantic_schema import RawInput

# Import modality detector
from ingestion.modality_detector import detect_modalities

# Import extractor registry
from routing.extractor_registry import EXTRACTOR_REGISTRY


def route_extractors(raw_input: RawInput):
    """
    Determines which extractors should be executed
    based on detected input modalities.
    """

    # Detect which modalities are present
    modalities = detect_modalities(raw_input)

    # List to store selected extractor functions
    selected_extractors = []

    # If text modality exists and extractor is registered
    if modalities["has_text"] and "text" in EXTRACTOR_REGISTRY:
        selected_extractors.append(EXTRACTOR_REGISTRY["text"])

    # If image modality exists and extractor is registered
    if modalities["has_images"] and "image" in EXTRACTOR_REGISTRY:
        selected_extractors.append(EXTRACTOR_REGISTRY["image"])

    # If document modality exists and extractor is registered
    if modalities["has_documents"] and "document" in EXTRACTOR_REGISTRY:
        selected_extractors.append(EXTRACTOR_REGISTRY["document"])

    # Return list of extractor callables
    return selected_extractors
