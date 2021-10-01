"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730394024"

from exercises.ex05.utils import only_evens, sub


def test_only_evens_mixed() -> None:
    """Only evens use case."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_only_evens_lengthy() -> None:
    """Only evens use case pt 2."""
    xs: list[int] = [10, 11, 12, 13, 14, 15, 16, 17, 18]
    assert only_evens(xs) == [10, 12, 14, 16, 18]


def test_only_evens_odd_trial() -> None:
    """Only evens edge case. Should return empty string."""
    xs: list[int] = [1, 5, 3]
    assert only_evens(xs) == []


def test_only_evens_all_evens() -> None:
    """Only evens edge case. Should return string back."""
    xs: list[int] = [4, 4, 4]
    assert only_evens(xs) == [4, 4, 4]


def test_sub_ideal_list() -> None:
    """Sub use case."""
    xs: list[int] = [0, 20, 30, 40]
    assert sub(xs, 1, 3) == [20, 30]


def test_sub_use_lengthy() -> None:
    """Sub use case, longer list"""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert sub(xs, 2, 6) == [3, 4, 5, 6]


def test_sub_start_is_neg() -> None:
    """Sub edge case, start is negative."""
    xs: list[int] = [0, 1, 2, 3, 5]
    assert sub(xs, -3, 3) == [0, 1, 2]


def test_sub_end_is_neg() -> None: 
    """Sub edge case, end is negative."""
    xs: list[int] = [0, 1, 2, 3, 5]
    assert sub(xs, 1, -3) == []


def test_sub_end_is_greater_than() -> None:
    """Sub edge case, should return empty string because end > length."""
    xs: list[int] = [0, 1, 2, 3, 5]
    assert sub(xs, 3, 6) == [3, 5]


def test_sub_list_is_empty() -> None: 
    """Sub edge case, should return empty string if input string is empty."""
    xs: list[int] = list()
    assert sub(xs, 0, 2) == []


def test_sub_start_is_greater() -> None:
    """Sub edge case, shoudl return empty list because start is > length."""
    xs: list[int] = [0, 1, 2, 3, 5]
    assert sub(xs, 7, 3) == []