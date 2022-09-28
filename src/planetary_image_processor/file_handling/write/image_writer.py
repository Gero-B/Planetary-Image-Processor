from typing import List, Union

import cv2

from .base import Writer


class ImageWriter(Writer):
    def write(self, obj: Union[cv2.Mat, List[cv2.Mat]], params: List[int] = None):
        return cv2.imwrite(self.path, obj, params=params)
