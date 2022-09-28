from typing import List, Union

import cv2
from planetary_image_processor.types.frame import Frame

from .base import Writer


class ImageWriter(Writer):
    def write(self, obj: Union[Frame, List[Frame]], params: List[int] = None):
        return cv2.imwrite(self.path, obj, params=params)
