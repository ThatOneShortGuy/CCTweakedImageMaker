from dataclasses import dataclass
from typing import BinaryIO, Iterable

import numpy as np

from .Serializable import Serializable
from .Compression import xor

@dataclass
class FrameData(Serializable):
    pixels: str

    @classmethod
    def from_label(cls, labels: Iterable[np.uint8]) -> 'FrameData':
        return cls(''.join(map(lambda x: hex(x)[-1], labels)))
    
    @classmethod
    def default_from_size(cls, width: int, height: int) -> 'FrameData':
        return cls('f' * width * height)
    
    def serialize(self) -> bytes:
        return bytes(map(lambda c: int(c, 16), self.pixels))
    
    @classmethod
    def read_from(cls, file: BinaryIO, width: int, height: int, previous_frame_data: bytes) -> 'FrameData':
        res = b''
        i = 0
        while True:
            s = file.read(1)
            count = s[0] // 16 + 1
            c = s[0] % 16
            res += bytes([c] * count)
            i += 1
            if len(res) == width * height:
                break
            elif len(res) > width * height:
                raise ValueError('Too many pixels')
        res = xor(previous_frame_data, res)
        return cls(''.join(map(lambda x: hex(x)[-1], res)))