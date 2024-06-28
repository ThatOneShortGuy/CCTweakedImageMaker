from dataclasses import dataclass

@dataclass
class Header:
    version: int
    width: int
    height: int
    framerate: float