from typing import Iterable

import cv2
from planetary_image_processor.types.frame import Frame

from .base import Reader


class VideoReader(Reader):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.reader = cv2.VideoCapture(path)

    def frames(self) -> Iterable[Frame]:
        while self.reader.isOpened():
            ret, frame = self.reader.read()
            if not ret:
                break
            yield frame
