from dataclasses import dataclass
from typing import Iterable
from .Header import Header
from .Frame import Frame

@dataclass
class Video:
    header: Header
    frames: Iterable[Frame]