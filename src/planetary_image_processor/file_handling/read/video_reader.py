from typing import Any, Iterable

import cv2

from .base import Reader


class VideoReader(Reader):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.reader = cv2.VideoCapture(path)

    def read(self) -> Any:
        return self.reader.read()

    def frames(self) -> Iterable[Any]:
        while self.reader.isOpened():
            ret, frame = self.read()
            if not ret:
                break
            yield frame
