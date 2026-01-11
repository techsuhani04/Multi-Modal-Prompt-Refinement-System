from routing.router import route_extractors
from refinement.merger import merge_signals
from refinement.prompt_builder import build_refined_prompt
from validation.validator import validate_refined_prompt
import extractors  # ensure registration


def run_pipeline(raw_input):
    # Step 5: Extraction
    extractor_classes = route_extractors(raw_input)
    extracted_signals = []

    for extractor_class in extractor_classes:
        extractor = extractor_class()
        result = extractor.extract(raw_input)
        if result:
            extracted_signals.append(result)

    # Step 6: Merge & refine
    merged = merge_signals(extracted_signals)
    refined_prompt = build_refined_prompt(merged)

    # Step 7: Validate
    validation_result = validate_refined_prompt(refined_prompt)

    return validation_result
