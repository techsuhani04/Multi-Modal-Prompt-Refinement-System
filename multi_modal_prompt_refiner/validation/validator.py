def validate_refined_prompt(refined_prompt: dict) -> dict:
    """
    Validates the refined prompt and decides acceptance or rejection.
    """

    issues = []

    core_intent = refined_prompt.get("core_intent")
    functional_requirements = refined_prompt.get("functional_requirements", [])
    technical_constraints = refined_prompt.get("technical_constraints", [])
    deliverables = refined_prompt.get("deliverables", [])
    assumptions = refined_prompt.get("assumptions", [])
    ambiguities = refined_prompt.get("ambiguities", [])

    # Check for minimum meaningful content
    if not core_intent and not (
        functional_requirements or technical_constraints or deliverables
    ):
        return {
            "status": "rejected",
            "issues": ["Input does not contain sufficient meaningful information"],
            "refined_prompt": None
        }

    # Warning conditions
    if len(assumptions) >= 3:
        issues.append("High number of assumptions inferred")

    if len(ambiguities) >= 2:
        issues.append("Multiple ambiguities detected")

    # Decide final status
    status = "accepted"
    if issues:
        status = "accepted_with_warnings"

    return {
        "status": status,
        "issues": issues,
        "refined_prompt": refined_prompt
    }
