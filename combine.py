import typing
from typing import Protocol
from abc import abstractmethod


@typing.runtime_checkable
class Combinable(Protocol):
    @abstractmethod
    def can_combine(self, other: "Combinable") -> bool:
        ...

    @abstractmethod
    def combine(self, other: "Combinable") -> "Combinable":
        ...
