from dataclasses import dataclass
from typing import BinaryIO, Callable, Generator, TypeVar

import numpy as np
from numpy.typing import NDArray

from .Serializable import Serializable


T = TypeVar('T')

@dataclass
class Colors(Serializable):
    red: int
    green: int
    blue: int

    def serialize(self) -> bytes:
        return bytes([self.red, self.green, self.blue])

@dataclass
class ColorInformation(Serializable):
    colors: list[Colors]

    @classmethod
    def from_cluster(cls, clusters: NDArray[np.uint8]) -> 'ColorInformation':
        return cls([Colors(red=r, green=g, blue=b) for r, g, b in clusters])
    
    def serialize(self) -> bytes:
        assert len(self.colors) == 16, f"Expected 16 colors, got {len(self.colors)}"
        return b''.join([color.serialize() for color in self.colors])

    @classmethod
    def default(cls) -> 'ColorInformation':
        colors = [
            Colors(int('F0', 16), int('F0', 16), int('F0', 16)),    #F0F0F0
            Colors(int('F2', 16), int('B2', 16), int('33', 16)),    #F2B233
            Colors(int('E5', 16), int('7F', 16), int('D8', 16)),    #E57FD8
            Colors(int('99', 16), int('B2', 16), int('F2', 16)),    #99B2F2
            Colors(int('DE', 16), int('DE', 16), int('6C', 16)),    #DEDE6C
            Colors(int('7F', 16), int('CC', 16), int('19', 16)),    #7FCC19
            Colors(int('F2', 16), int('B2', 16), int('CC', 16)),    #F2B2CC
            Colors(int('4C', 16), int('4C', 16), int('4C', 16)),    #4C4C4C
            Colors(int('99', 16), int('99', 16), int('99', 16)),    #999999
            Colors(int('4C', 16), int('99', 16), int('B2', 16)),    #4C99B2
            Colors(int('B2', 16), int('66', 16), int('E5', 16)),    #B266E5
            Colors(int('33', 16), int('66', 16), int('CC', 16)),    #3366CC
            Colors(int('7F', 16), int('66', 16), int('4C', 16)),    #7F664C
            Colors(int('57', 16), int('A6', 16), int('4E', 16)),    #57A64E
            Colors(int('CC', 16), int('4C', 16), int('4C', 16)),    #CC4C4C
            Colors(int('11', 16), int('11', 16), int('11', 16)),    #111111
        ]
        return cls(colors)

    @classmethod
    def read_from(cls, file: BinaryIO) -> 'ColorInformation':
        colors = [Colors(red=int.from_bytes(file.read(1), 'little'),
                         green=int.from_bytes(file.read(1), 'little'),
                         blue=int.from_bytes(file.read(1), 'little')) for _ in range(16)]
        return cls(colors)
    
    def map(self, fn: Callable[[Colors], T]) -> Generator[T, None, None]:
        return (fn(color) for color in self.colors)