from glob import glob
from typing import Iterable

from planetary_image_processor.file_handling.read.media_reader import MediaReader
from planetary_image_processor.types.frame import Frame

from .base import Reader


class DirectoryReader(Reader):
    def __init__(self, path: str, recursive=None) -> None:
        super().__init__(path)
        self.paths = glob(path, recursive=recursive)

    def frames(self) -> Iterable[Frame]:
        for path in self.paths:
            reader = MediaReader(path)
            for frame in reader.frames():
                yield frame
