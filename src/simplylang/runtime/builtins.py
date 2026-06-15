from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable


BuiltinFunction = Callable[..., object]


@dataclass
class Builtins:
    functions: dict[str, BuiltinFunction] = field(default_factory=dict)

    def register(self, name: str, function: BuiltinFunction) -> None:
        self.functions[name] = function

    def get(self, name: str) -> BuiltinFunction | None:
        return self.functions.get(name)


def default_builtins() -> Builtins:
    return Builtins()
