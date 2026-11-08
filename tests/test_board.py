from pythonlearning_chess_project.board import STARTING_FEN


def test_starting_fen_has_six_fields() -> None:
    assert len(STARTING_FEN.split()) == 6
