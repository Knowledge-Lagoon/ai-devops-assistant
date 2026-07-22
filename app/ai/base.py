from abc import ABC, abstractmethod


class AIProvider(ABC):
    """Abstract base class for AI providers."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response for the given prompt."""
        raise NotImplementedError
