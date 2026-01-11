from abc import ABC, abstractmethod


class BaseExtractor(ABC):
    """
    Base contract for all modality extractors.
    """

    @abstractmethod
    def extract(self, raw_input) -> dict:
        """
        Must return data following the unified extraction schema.
        """
        pass
