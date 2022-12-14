import os
from typing import Iterable

from planetary_image_processor.file_handling.constants import IMAGE_FORMATS, VIDEO_FORMATS
from planetary_image_processor.types.frame import Frame

from .base import Reader
from .image_reader import ImageReader
from .video_reader import VideoReader


class MediaReader(Reader):
    location = None
    readers = {IMAGE_FORMATS: ImageReader, VIDEO_FORMATS: VideoReader}

    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.reader = self.get_reader(path)

    @classmethod
    def get_reader(cls, path: str) -> Reader:
        _, ext = os.path.splitext(path)
        for fmts, Reader_ in cls.readers.items():
            if ext in fmts:
                return Reader_(path)

    def frames(self) -> Iterable[Frame]:
        return self.reader.frames()
