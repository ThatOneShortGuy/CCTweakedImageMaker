import struct
from dataclasses import dataclass

from .Serializable import Serializable


@dataclass
class Header(Serializable):
    version: int
    width: int
    height: int
    framerate: float

    def serialize(self) -> bytes:
        return b'ccvid'+f'{self.version:02d}'.encode() + self.width.to_bytes(2, 'little') + self.height.to_bytes(2, 'little') + struct.pack('f', self.framerate)
