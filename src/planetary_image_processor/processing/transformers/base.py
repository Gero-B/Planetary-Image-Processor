from abc import ABC, abstractmethod
from typing import Any


class Transformer(ABC):
    @abstractmethod
    def apply(self, obj: Any) -> Any:
        ...
