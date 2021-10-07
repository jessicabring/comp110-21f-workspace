"""Practice with dictionaries."""

__author__ = "730394024"

# Define your functions below.


def invert(map: dict[str, str]) -> dict[str, str]:
    result: dict[str, str] = dict()
    for key in map:
        result[key] = map[key]
    return result