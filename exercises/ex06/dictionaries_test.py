"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730394024"


def test_invert_duplicate_keys() -> None:
    """Edge case: tests for duplicate keys."""
    input: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
    assert invert(input) == KeyError('KeyError')


def test_invert_long() -> None: 
    """Use case with a longer dictionary input."""
    input: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w'}
    assert invert(input) == {'z': 'a', 'y': 'b', 'x': 'c', 'w': 'd'}


def test_invert_normal() -> None:
    """Use case with average input."""
    input: dict[str, str] = {'apple': 'cat', 'banana': 'fish', 'peach': 'dog'}
    assert invert(input) == {'cat': 'apple', 'fish': 'banana', 'dog': 'peach'}


def test_favorite_color_tie() -> None:
    """Edge case, when two colors are tied."""
    input: dict[str, str] = {"Jessica": "black", "Grace": "blue", "Cece": "red", "Rhiannon": "red", "Rachael": "blue"}
    assert favorite_color(input) == "black"


def test_favorite_color_short() -> None:
    """Use case, short dictionary input."""
    input: dict[str, str] = {'Jessica': 'black', 'Michelle': 'black', 'Grace': 'red'}
    assert favorite_color(input) == "black"


def test_favorite_color_long() -> None:
    """Use case, longer string with many contenders."""
    input: dict[str, str] = {'Jessica': 'black', 'Michelle': 'red', 'Grace': 'red', 'Rachael': 'red', 'Rhiannon': 'green', 'Cece': 'green', 'Katy': 'black'}
    assert favorite_color(input) == "red"


def test_count_no_duplicates() -> None:
    """Edge case, no duplicate values in the list input."""
    input: list[str] = ['the', 'quick', 'brown', 'fox']
    assert count(input) == {'the': 1, 'quick': 1, 'brown': 1, 'fox': 1}


def test_count_long_list() -> None:
    """Use case with a longer list input."""
    input: list[str] = ["earth", "wind", "fire", "wind", "fire", "wind"]
    assert count(input) == {'earth': 1, 'wind': 3, 'fire': 2}


def test_count_repeated_list() -> None:
    """Use case with regular length, all one term."""
    input: list[str] = ["hi", "hi", "hi", "hi", "hi"]
    assert count(input) == {'hi': 5}
