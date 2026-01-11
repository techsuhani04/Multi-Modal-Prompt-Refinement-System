def merge_signals(extracted_signals: list) -> dict:
    """
    Merges modality-specific extracted signals into a unified representation.
    """

    merged = {
        "intent_candidates": [],
        "functional_requirements": [],
        "technical_constraints": [],
        "deliverables": [],
        "ambiguities": [],
        "sources_used": []
    }

    for signal in extracted_signals:
        source = signal.get("source_modality")
        confidence = signal.get("confidence", 0)

        merged["sources_used"].append(source)

        # Collect intents with confidence
        if signal.get("intent"):
            merged["intent_candidates"].append(
                (signal["intent"], confidence, source)
            )

        merged["functional_requirements"].extend(
            signal.get("functional_requirements", [])
        )

        merged["technical_constraints"].extend(
            signal.get("technical_constraints", [])
        )

        merged["deliverables"].extend(
            signal.get("deliverables", [])
        )

    # Resolve intent using highest confidence
    if merged["intent_candidates"]:
        merged["intent_candidates"].sort(key=lambda x: x[1], reverse=True)
        resolved_intent = merged["intent_candidates"][0][0]
    else:
        resolved_intent = None
        merged["ambiguities"].append("No clear intent detected")

    return {
        "core_intent": resolved_intent,
        "functional_requirements": list(set(merged["functional_requirements"])),
        "technical_constraints": list(set(merged["technical_constraints"])),
        "deliverables": list(set(merged["deliverables"])),
        "ambiguities": merged["ambiguities"],
        "sources_used": list(set(merged["sources_used"]))
    }
