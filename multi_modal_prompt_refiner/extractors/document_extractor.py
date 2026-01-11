from normalization.semantic_schema import RawInput
from routing.extractor_registry import register_extractor
from extractors.base import BaseExtractor


@register_extractor("document")
class DocumentExtractor(BaseExtractor):

    def extract(self, raw_input: RawInput) -> dict:
        if not raw_input.documents:
            return {}

        document_names = [doc.filename for doc in raw_input.documents]

        return {
            "source_modality": "document",
            "intent": "Formal specifications provided",
            "functional_requirements": [],
            "technical_constraints": [
                f"Refer to specifications in {name}" for name in document_names
            ],
            "deliverables": [],
            "confidence": 0.85
        }
