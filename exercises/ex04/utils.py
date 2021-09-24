"""List utility functions."""

__author__ = "730394024"


# TODO: Implement your functions here.

def all(a: list[int], b: int) -> bool:
    """Determines if all values in a list are equal to the integer in the argument."""
    i: int = 0
    while len(a) > 0: 
        while i < len(a):
            if a[i] == b:
                i += 1
            else: 
                return False
        if i == len(a):
            return True
        return False
    else: 
        return False


def is_equal(a: list[int], b: list[int]) -> bool: 
    """Compares two lists, returns True if they are equal to each other and False if not."""
    i: int = 0
    while len(a) == len(b):
        while i < len(a):
            if a[i] == b[i]:
                i += 1
            else:
                return False
    
        if i == len(a):
            return True
    else: 
        return False
    

def max(input: list[int]) -> int:
    """Finds the largest value in a given list, returns its' value."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else: 
        i: int = 0
        list_max: int = input[0]
        while i < len(input) - 1:
            if list_max < input[i + 1]:
                list_max = input[i + 1]
            i += 1
        return list_max
