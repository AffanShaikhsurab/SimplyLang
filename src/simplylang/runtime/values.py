from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class RuntimeValue:
    value: Any

    def copy(self) -> "RuntimeValue":
        return type(self)(self.value)


@dataclass(frozen=True)
class NumberValue(RuntimeValue):
    value: int | float


@dataclass(frozen=True)
class BoolValue(RuntimeValue):
    value: bool


@dataclass(frozen=True)
class FunctionValue:
    name: str
    parameters: tuple[str, ...]
    body: tuple[object, ...]


@dataclass(frozen=True)
class ClassValue:
    name: str
    fields: tuple[str, ...]
    body: tuple[object, ...]


@dataclass(frozen=True)
class ContractValue:
    name: str
    parameters: tuple[str, ...]
    body: tuple[object, ...]
