def build_refined_prompt(merged_data: dict) -> dict:
    """
    Builds the final refined prompt structure.
    """

    assumptions = []

    if not merged_data["functional_requirements"]:
        assumptions.append("Functional requirements were not explicitly specified")

    if not merged_data["technical_constraints"]:
        assumptions.append("No technical constraints were provided")

    if not merged_data["deliverables"]:
        assumptions.append("Deliverables were inferred implicitly")

    return {
        "core_intent": merged_data["core_intent"],
        "functional_requirements": merged_data["functional_requirements"],
        "technical_constraints": merged_data["technical_constraints"],
        "deliverables": merged_data["deliverables"],
        "assumptions": assumptions,
        "ambiguities": merged_data["ambiguities"],
        "sources_used": merged_data["sources_used"]
    }
