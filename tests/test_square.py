import pytest

from pythonlearning_chess_project.square import Square


def test_square_from_name() -> None:
    assert Square.from_name("a1") == Square(0, 0)
    assert Square.from_name("e4") == Square(4, 3)
    assert Square.from_name("h8") == Square(7, 7)


def test_square_name() -> None:
    assert Square(4, 3).name == "e4"


@pytest.mark.parametrize("name", ["", "e", "e9", "i1", "e44"])
def test_invalid_name_is_rejected(name: str) -> None:
    with pytest.raises(ValueError):
        Square.from_name(name)


def test_square_off_the_board_is_rejected() -> None:
    with pytest.raises(ValueError):
        Square(8, 0)
