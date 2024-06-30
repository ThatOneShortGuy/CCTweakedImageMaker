from dataclasses import dataclass
from typing import Iterable

from .Frame import Frame
from .Header import Header
from .Serializable import Serializable


@dataclass
class Video(Serializable):
    header: Header
    frames: Iterable[Frame]

    def serialize(self) -> bytes:
        return self.header.serialize() + b''.join(frame.serialize() for frame in self.frames)
