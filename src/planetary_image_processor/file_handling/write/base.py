from abc import ABC, abstractmethod
from typing import Any


class Writer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def write(self, obj: Any):
        ...
