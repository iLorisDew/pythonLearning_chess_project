from dataclasses import dataclass
from typing import Self

FILES = "abcdefgh"
RANKS = "12345678"


@dataclass(frozen=True)
class Square:
    file: int  # 0 = file a ... 7 = file h
    rank: int  # 0 = rank 1 ... 7 = rank 8

    def __post_init__(self) -> None:
        if not (0 <= self.file <= 7 and 0 <= self.rank <= 7):
            raise ValueError(f"Square off the board: file={self.file}, rank={self.rank}")

    @classmethod
    def from_name(cls, name: str) -> Self:
        if len(name) != 2 or name[0] not in FILES or name[1] not in RANKS:
            raise ValueError(f"Invalid square name: {name!r}")
        return cls(FILES.index(name[0]), RANKS.index(name[1]))

    @property
    def name(self) -> str:
        return FILES[self.file] + RANKS[self.rank]
