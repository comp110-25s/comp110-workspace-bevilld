"""Tests our third coding exercise"""

__author__: str = "730509911"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_Use1() -> None:
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_Use2() -> None:
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_Edge() -> None:
    assert invert({}) == {}


def test_count_Edge() -> None:
    assert count([]) == {}


def test_count_Use1() -> None:
    assert count(["cat"]) == {"cat": 1}


def test_count_Use2() -> None:
    assert count(["dog", "dog", "cat", "cat"]) == {"dog": 2, "cat": 2}


def test_favorite_color_Use1() -> None:
    assert favorite_color({"Howard": "red", "Chuck": "blue", "Saul": "blue"}) == "blue"


def test_favorite_color_Use2() -> None:
    assert favorite_color({"Jimmy": "red", "Kim": "blue"}) == "red"


def test_favorite_color_Edge() -> None:
    assert favorite_color({}) == ""


def test_bin_len_Use1() -> None:
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_Use2() -> None:
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_Edge() -> None:
    assert bin_len([]) == {}
