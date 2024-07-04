import struct
from dataclasses import dataclass
from typing import BinaryIO

from .Serializable import Serializable


@dataclass
class Header(Serializable):
    version: int
    width: int
    height: int
    framerate: float

    def serialize(self) -> bytes:
        return b'ccvid'+f'{self.version:02d}'.encode() + self.width.to_bytes(2, 'little') + self.height.to_bytes(2, 'little') + struct.pack('f', self.framerate)
    
    @classmethod
    def read_from(cls, f: BinaryIO):
        magic = f.read(5)
        if magic != b'ccvid':
            raise ValueError('Invalid magic code')
        version = int(f.read(2).decode())
        width = int.from_bytes(f.read(2), 'little')
        height = int.from_bytes(f.read(2), 'little')
        framerate = struct.unpack('f', f.read(4))[0]
        return cls(version, width, height, framerate)
