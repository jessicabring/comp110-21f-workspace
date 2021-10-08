"""Practice with dictionaries."""

__author__ = "730394024"

# Define your functions below.


def invert(map: dict[str, str]) -> dict[str, str]:
    """Takes a dictionary and switches the keys with the values and vice versa."""
    result: dict[str, str] = dict()
    for key in map:
        if map[key] in result:
            raise KeyError('KeyError')
        result[map[key]] = key
    return result


def favorite_color(log: dict[str, str]) -> str:
    """Takes a dictionary and returns the value with highest frequency."""
    counter: int = 0
    result: str = "" 
    first_value: str = ""
    color_winner: int = 0
    val_1: str
    is_duplicate: bool = False

    for key in log:
        val_1 = log[key]
        if counter == 0: 
            first_value = log[key]
            counter += 1
        for dup in log:
            if log[dup] == val_1:
                counter += 1
            if counter > 2:    
                is_duplicate = True
        if counter == color_winner and is_duplicate is False:
            result = first_value
        if counter > color_winner:
            result = log[key]
            color_winner = counter
        
        counter = 1
        is_duplicate = False
    
    return result


def count(a: list[str]) -> dict[str, int]:
    """Tracks how many times a value is in a list, returns a dictionary with the list values as keys and frequency as values."""
    i: int = 0
    key: str
    result: dict[str, int] = dict()
    while i < len(a):
        key = a[i]
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
        i += 1
    return result
        