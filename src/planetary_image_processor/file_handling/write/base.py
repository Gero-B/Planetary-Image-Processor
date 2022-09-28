from abc import ABC, abstractmethod
from typing import Iterable, Union

from planetary_image_processor.types.frame import Frame


class Writer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def write(self, obj: Union[Frame, Iterable[Frame]]):
        ...
