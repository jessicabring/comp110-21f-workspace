"""List utility functions."""

__author__ = "730394024"


# TODO: Implement your functions here.

def all(a: list[int], b: int) -> bool:
    i: int = 0
    while i < len(a):
        if a[i] == b:
            i += 1
        else: 
            return False
    if i == len(a):
        return True
    return False


def is_equal(a: list[int], b: list[int]) -> bool: 
    i: int = 0
    while i < len(a):
        if a[i] == b[i]:
            i += 1
        else:
            return False
    
    if i == len(a):
        return True
    else: 
        return False
    

def max(a: list[int]) -> int:
    if len(a) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    list_max: int = a[0]
    while i < len(a) - 1:
        if list_max < a[i + 1]:
            list_max = a[i + 1]
        i += 1
    return list_max
