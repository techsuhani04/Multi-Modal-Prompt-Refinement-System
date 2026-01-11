from normalization.semantic_schema import RawInput
from routing.extractor_registry import register_extractor
from extractors.base import BaseExtractor


@register_extractor("image")
class ImageExtractor(BaseExtractor):

    def extract(self, raw_input: RawInput) -> dict:
        if not raw_input.images:
            return {}

        image_names = [img.filename for img in raw_input.images]

        # No hard assumptions here
        inferred_intent = "Visual reference provided for design or layout guidance"

        return {
            "source_modality": "image",
            "intent": inferred_intent,
            "functional_requirements": [],
            "technical_constraints": [],
            "deliverables": [f"Design inspired by {', '.join(image_names)}"],
            "confidence": 0.6
        }
