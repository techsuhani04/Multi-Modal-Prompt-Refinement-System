# Import typing helper
from typing import Callable, Dict


# Registry mapping modality names to extractor functions
EXTRACTOR_REGISTRY: Dict[str, Callable] = {}


def register_extractor(modality: str):
    """
    Decorator to register an extractor function for a given modality.
    """

    def decorator(func: Callable):
        # Store extractor function in the registry
        EXTRACTOR_REGISTRY[modality] = func
        return func

    return decorator
