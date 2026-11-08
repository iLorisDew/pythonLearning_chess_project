from pythonlearning_chess_project.board import STARTING_FEN, Board
from pythonlearning_chess_project.pieces import Color, Piece, PieceType
from pythonlearning_chess_project.square import Square


def test_starting_fen_has_six_fields() -> None:
    assert len(STARTING_FEN.split()) == 6


def test_new_board_is_empty() -> None:
    board = Board()
    assert board.piece_at(Square.from_name("e1")) is None


def test_set_then_get_piece() -> None:
    board = Board()
    king = Piece(Color.WHITE, PieceType.KING)
    board.set_piece(Square.from_name("e1"), king)
    assert board.piece_at(Square.from_name("e1")) == king
