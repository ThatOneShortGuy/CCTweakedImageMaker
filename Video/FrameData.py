from dataclasses import dataclass
from typing import Iterable

import numpy as np

from .Serializable import Serializable

@dataclass
class FrameData(Serializable):
    pixels: str

    @classmethod
    def from_label(cls, labels: Iterable[np.uint8]) -> 'FrameData':
        return cls(''.join(map(lambda x: hex(x)[-1], labels)))