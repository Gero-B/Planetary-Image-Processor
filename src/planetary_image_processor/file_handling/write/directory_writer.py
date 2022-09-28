from typing import Iterable, Union

from planetary_image_processor.file_handling.constants import IMAGE_FORMATS
from planetary_image_processor.types.frame import Frame

from .base import Writer
from .image_writer import ImageWriter


class DirectoryWriter(Writer):
    writers = {IMAGE_FORMATS: ImageWriter}

    def __init__(
        self, path: str, prefix: str = "", ext: str = ".tif", format_num: str = "{:02d}"
    ) -> None:
        super().__init__(path)
        self.formatter = f"{path}/{prefix}_{format_num}{ext}"
        self.Writer = self.get_writer(ext)  # pylint:disable=invalid-name
        if not self.Writer:
            raise ValueError(f"Could not find Writer for ext {ext}")
        self.count = 0

    @classmethod
    def get_writer(cls, ext):
        for fmts, Writer_ in cls.writers.items():
            if ext in fmts:
                return Writer_
        return None

    @property
    def writer(self) -> Writer:
        path = self.formatter.format(self.count)
        return self.Writer(path)

    def write(self, obj: Union[Frame, Iterable[Frame]]):
        self.writer.write(obj)
        self.count += 1
