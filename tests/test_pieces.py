import pytest

from pythonlearning_chess_project.pieces import Color, Piece, PieceType


def test_color_from_fen_letter() -> None:
    assert Color("w") is Color.WHITE
    assert Color("b") is Color.BLACK


def test_white_knight_from_symbol() -> None:
    assert Piece.from_symbol("N") == Piece(Color.WHITE, PieceType.KNIGHT)


def test_black_queen_from_symbol() -> None:
    assert Piece.from_symbol("q") == Piece(Color.BLACK, PieceType.QUEEN)


@pytest.mark.parametrize("symbol", list("PNBRQKpnbrqk"))
def test_symbol_round_trip(symbol: str) -> None:
    assert Piece.from_symbol(symbol).symbol == symbol


def test_unknown_symbol_is_rejected() -> None:
    with pytest.raises(ValueError):
        Piece.from_symbol("x")
