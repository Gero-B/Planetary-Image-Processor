from abc import ABC, abstractmethod
from typing import Iterable

from planetary_image_processor.types.frame import Frame


class Reader(ABC):
    path = None

    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def frames(self) -> Iterable[Frame]:
        ...
