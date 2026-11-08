from dataclasses import dataclass
from enum import Enum
from typing import Self

class Color(Enum):
    BLACK = "b"
    WHITE = "w"
    
class PieceType(Enum):
    PAWN = "p"
    KNIGHT = "n"
    BISHOP = "b"
    ROOK = "r"
    QUEEN = "q"
    KING = "k"
    
@dataclass(frozen=True)
class Piece:
    color: Color
    kind: PieceType
    
    @classmethod
    def from_symbol(cls, symbol: str) -> Self:
        color = Color.WHITE if symbol.isupper() else Color.BLACK
        return cls(color, PieceType(symbol.lower()))

    @property
    def symbol(self) -> str:
        letter = self.kind.value
        return letter.upper() if self.color is Color.WHITE else letter