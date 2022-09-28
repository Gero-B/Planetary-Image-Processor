from typing import Iterable

import cv2
from planetary_image_processor.types.frame import Frame

from .base import Reader


class ImageReader(Reader):
    def frames(self, flags=None) -> Iterable[Frame]:
        yield cv2.imread(self.path, flags=flags)
