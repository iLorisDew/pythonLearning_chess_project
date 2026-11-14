from pythonlearning_chess_project.board import STARTING_FEN, Board
from pythonlearning_chess_project.pieces import Color, Piece, PieceType
from pythonlearning_chess_project.square import Square
import pytest

REFERENCE_FENS = [
    STARTING_FEN,
    "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1",
    "r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1",
    "8/2p5/3p4/KP5r/1R3p1k/8/4P1P1/8 w - - 0 1",
    "rnbq1k1r/pp1Pbppp/2p5/8/2B5/8/PPP1NnPP/RNBQK2R w KQ - 1 8",
]


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


def test_from_fen_places_pieces() -> None:
    board = Board.from_fen(STARTING_FEN)
    assert board.piece_at(Square.from_name("e1")) == Piece(Color.WHITE, PieceType.KING)
    assert board.piece_at(Square.from_name("d8")) == Piece(Color.BLACK, PieceType.QUEEN)
    assert board.piece_at(Square.from_name("a2")) == Piece(Color.WHITE, PieceType.PAWN)
    assert board.piece_at(Square.from_name("e4")) is None


def test_from_fen_reads_game_state() -> None:
    board = Board.from_fen("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1")
    assert board.turn is Color.BLACK
    assert board.castling == "KQkq"
    assert board.en_passant == Square.from_name("e3")
    assert board.halfmove_clock == 0
    assert board.fullmove_number == 1

def test_empty_board_to_fen() -> None:
    assert Board().to_fen() == "8/8/8/8/8/8/8/8 w - - 0 1"

@pytest.mark.parametrize("fen", REFERENCE_FENS)
def test_fen_round_trip(fen: str) -> None:
    assert Board.from_fen(fen).to_fen() == fen

@pytest.mark.parametrize(
    "fen",
    [
        "",  # empty
        "8/8/8/8/8/8/8/8 w - -",  # 4 fields instead of 6
        "8/8/8/8/8/8/8 w - - 0 1",  # 7 rows instead of 8
        "9/8/8/8/8/8/8/8 w - - 0 1",  # a row of 9 squares
        "8/8/8/8/8/8/8/8 x - - 0 1",  # "x" is not a color
        "8/8/8/8/8/8/8/7X w - - 0 1",  # "X" is not a piece
    ],
)
def test_invalid_fen_is_rejected(fen: str) -> None:
    with pytest.raises(ValueError):
        Board.from_fen(fen)