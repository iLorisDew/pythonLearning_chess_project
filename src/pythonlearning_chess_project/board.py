from pythonlearning_chess_project.pieces import Color, Piece
from pythonlearning_chess_project.square import Square

STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"


class Board:
    def __init__(self) -> None:
        # _grid[rank][file] -- rank 0 is the white side
        self._grid: list[list[Piece | None]] = [[None] * 8 for _ in range(8)]
        self.turn = Color.WHITE
        self.castling = ""  # e.g. "KQkq"; "" means no castling rights
        self.en_passant: Square | None = None
        self.halfmove_clock = 0
        self.fullmove_number = 1

    def piece_at(self, square: Square) -> Piece | None:
        return self._grid[square.rank][square.file]

    def set_piece(self, square: Square, piece: Piece | None) -> None:
        self._grid[square.rank][square.file] = piece
