from normalization.semantic_schema import RawInput
from routing.extractor_registry import register_extractor
from extractors.base import BaseExtractor


@register_extractor("text")
class TextExtractor(BaseExtractor):

    def extract(self, raw_input: RawInput) -> dict:
        text = raw_input.text

        if not text:
            return {}

        # Placeholder logic (LLM-based later)
        intent = text.split(".")[0]  # naive heuristic
        functional_requirements = []
        technical_constraints = []
        deliverables = []

        # Simple keyword-based heuristics
        for line in text.split("\n"):
            if "must" in line.lower():
                functional_requirements.append(line.strip())
            if "constraint" in line.lower():
                technical_constraints.append(line.strip())
            if "deliver" in line.lower():
                deliverables.append(line.strip())

        return {
            "source_modality": "text",
            "intent": intent,
            "functional_requirements": functional_requirements,
            "technical_constraints": technical_constraints,
            "deliverables": deliverables,
            "confidence": 0.9
        }
