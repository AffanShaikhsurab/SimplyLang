from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any


class OpCode(Enum):
    CONSTANT = auto()
    LOAD_NAME = auto()
    STORE_NAME = auto()
    CALL = auto()
    RETURN = auto()
    POP = auto()


@dataclass(frozen=True)
class Instruction:
    opcode: OpCode
    operand: Any = None
    line: int | None = None


@dataclass
class Chunk:
    instructions: list[Instruction] = field(default_factory=list)
    constants: list[Any] = field(default_factory=list)

    def add_constant(self, value: Any) -> int:
        self.constants.append(value)
        return len(self.constants) - 1

    def emit(
        self, opcode: OpCode, operand: Any = None, line: int | None = None
    ) -> None:
        self.instructions.append(Instruction(opcode, operand, line))
