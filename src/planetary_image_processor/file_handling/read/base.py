from abc import ABC, abstractmethod
from typing import Any, Iterable

import cv2


class Reader(ABC):
    path = None

    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def read(self) -> Any:
        ...

    @abstractmethod
    def frames(self) -> Iterable[cv2.Mat]:
        ...
