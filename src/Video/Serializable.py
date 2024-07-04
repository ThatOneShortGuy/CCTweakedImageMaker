from typing import Protocol
from abc import abstractmethod

class Serializable(Protocol):
    @abstractmethod
    def serialize(self) -> bytes:
        ...
