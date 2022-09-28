from typing import Any, Iterable

import cv2

from .base import Reader


class ImageReader(Reader):
    def read(self, flags=None) -> Any:
        return cv2.imread(self.path, flags=flags)

    def frames(self, **kwargs) -> Iterable[Any]:
        return [self.read(**kwargs)]
