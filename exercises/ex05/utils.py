"""List utility functions part 2."""

__author__ = "730394024"


def only_evens(a: list[int]) -> list[int]:
    """Function that takes a list of integers and returns a new list with only even integers."""
    result: list[int] = list()
    for x in a:
        if x % 2 == 0:
            result.append(x)
    return result


def sub(x: list[int], start: int, end: int) -> list[int]:
    """Function that takes a list input and bounds and returns a new list with the numbers in between the given bounds."""
    result: list[int] = list()
    i: int = 0
    if end > len(x):
        end = len(x)
    if len(x) == 0: 
        return result
    else: 
        if start > len(x):
            return result
        else: 
            if end <= 0:
                return result
    while i < end:
        if i >= start:
            result.append(x[i])
        else: 
            if start < 0:
                result.append(x[i])
        i += 1
    return result


def concat(a: list[int], b: list[int]) -> list[int]:
    result: list[int] = list()
    if len(a) == 0:
        return result
    else: 
        if len(b) == 0:
            return result

    for x in a:
        result.append(x)
    for y in b: 
        result.append(y)
    return result
