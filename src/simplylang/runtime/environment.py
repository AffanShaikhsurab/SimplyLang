from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class Environment:
    values: dict[str, Any] = field(default_factory=dict)
    parent: Optional["Environment"] = None

    def get(self, name: str) -> Any:
        if name in self.values:
            return self.values[name]
        if self.parent:
            return self.parent.get(name)
        return None

    def set(self, name: str, value: Any) -> None:
        self.values[name] = value

    def remove(self, name: str) -> None:
        del self.values[name]
