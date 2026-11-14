from pythonlearning_chess_project.pieces import Color, Piece
from pythonlearning_chess_project.square import Square
from typing import Self

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



    @classmethod 
    def from_fen(cls, fen: str) -> Self:
        fields = fen.split()
        if len(fields) != 6:
            raise ValueError(f"FEN must have 6 fields, got {len(fields)}: {fen!r}")
        placement, turn, castling, en_passant, halfmove, fullmove = fields

        rows = placement.split("/")
        if len(rows) != 8:
            raise ValueError(f"FEN placement must have 8 rows, got {len(rows)}")

        board = cls()
        for index, row in enumerate(rows):
            rank = 7 - index  # the first row of the FEN is rank 8
            file = 0
            for char in row:
                if char.isdigit():
                    file += int(char)
                else:
                    board.set_piece(Square(file, rank), Piece.from_symbol(char))
                    file += 1
            if file != 8:
                raise ValueError(f"FEN row {row!r} does not cover 8 squares")

        board.turn = Color(turn)
        board.castling = "" if castling == "-" else castling
        board.en_passant = None if en_passant == "-" else Square.from_name(en_passant)
        board.halfmove_clock = int(halfmove)
        board.fullmove_number = int(fullmove)
        return board

    def to_fen(self) -> str:
        rows: list[str] = []
        for rank in range(7, -1, -1):
            row = ""
            empty = 0
            for file in range(8):
                piece = self._grid[rank][file]
                if piece is None:
                    empty += 1
                else:
                    if empty > 0:
                        row += str(empty)
                        empty = 0
                    row += piece.symbol
            if empty > 0:
                row += str(empty)
            rows.append(row)

        fields = [
            "/".join(rows),
            self.turn.value,
            self.castling or "-",
            self.en_passant.name if self.en_passant else "-",
            str(self.halfmove_clock),
            str(self.fullmove_number),
        ]
        return " ".join(fields)




        
    


