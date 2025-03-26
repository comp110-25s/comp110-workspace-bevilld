"""Tests our third coding exercise"""

__author__: str = "730509911"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert() -> None:
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}
    assert invert({"apple": "cat"}) == {"cat": "apple"}
    assert invert({}) == {}


def test_count() -> None:
    assert count([]) == {}
    assert count(["cat"]) == {"cat": 1}
    assert count(["dog", "dog", "cat", "cat"]) == {"dog": 2, "cat": 2}


def test_favorite_color() -> None:
    assert favorite_color({"Howard": "red", "Chuck": "blue", "Saul": "blue"}) == {
        "blue"
    }
    assert favorite_color({"Jimmy": "red", "Kim": "blue"}) == {"red"}
    assert favorite_color({}) == ""


def test_bin_len() -> None:
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}
    assert bin_len([]) == {}
