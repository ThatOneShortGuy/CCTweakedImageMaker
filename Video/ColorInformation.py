from dataclasses import dataclass
from typing import Iterable

import numpy as np
from numpy.typing import NDArray

from .Serializable import Serializable


@dataclass
class Colors:
    red: int
    green: int
    blue: int

@dataclass
class ColorInformation(Serializable):
    colors: Iterable[Colors]

    @classmethod
    def from_cluster(cls, clusters: NDArray[np.uint8]) -> 'ColorInformation':
        return cls([Colors(red=r, green=g, blue=b) for r, g, b in clusters])