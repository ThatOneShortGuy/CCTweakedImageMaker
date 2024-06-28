from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from compute import get_code_from_ndarray

from .ColorInformation import ColorInformation
from .FrameData import FrameData


@dataclass
class Frame:
    color_information: ColorInformation
    frame_data: FrameData

    @classmethod
    def from_ndarray(cls, ndarray: NDArray[np.uint8]) -> 'Frame':
        labels, clusters = get_code_from_ndarray(ndarray)
        return cls(ColorInformation.from_cluster(clusters), FrameData.from_label(labels))
