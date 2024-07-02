from dataclasses import dataclass
from typing import BinaryIO

import numpy as np
from numpy.typing import NDArray

from compute import get_code_from_ndarray
import cv2 as cv

from .ColorInformation import ColorInformation
from .FrameData import FrameData
from .Serializable import Serializable


@dataclass
class Frame(Serializable):
    color_information: ColorInformation
    frame_data: FrameData

    @classmethod
    def from_ndarray(cls, ndarray: NDArray[np.uint8]) -> 'Frame':
        labels, clusters = get_code_from_ndarray(ndarray)
        return cls(ColorInformation.from_cluster(clusters), FrameData.from_label(labels))
    
    def serialize(self) -> bytes:
        return self.color_information.serialize() + self.frame_data.serialize()
    
    @classmethod
    def read_from(cls, file: BinaryIO, width: int, height: int, previous_frame_data: bytes):
        color_information = ColorInformation.read_from(file)
        frame_data = FrameData.read_from(file, width, height, previous_frame_data)
        return cls(color_information, frame_data)

    def display(self, title: str, width: int, height: int):
        colors = {i: c for i, c in enumerate(self.color_information.map(lambda color: (color.red, color.green, color.blue)))}
        pixels = list(map(lambda x: colors[int(x, 16)], self.frame_data.pixels))
        img = np.array(pixels, dtype=np.uint8).reshape((height, width, 3))
        img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
        target_width = 1200
        target_height = int(height * target_width / width)
        img = cv.resize(img, (target_width, target_height), interpolation=cv.INTER_NEAREST)
        cv.imshow(title, img)
        cv.waitKey(69)
    
    @staticmethod
    def close_display():
        cv.destroyAllWindows()