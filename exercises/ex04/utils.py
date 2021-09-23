"""List utility functions."""

__author__ = "730394024"


# TODO: Implement your functions here.

def main() -> None:
    print(all([1, 2, 3], 2))
    print(is_equal([1, 0, 1], [1, 0, 1]))
    print(is_equal([1, 1, 0, 4], [1, 0, 1, 4]))


def all(a: list[int], b: int) -> bool:
    i: int = 0
    while i < len(a):
        if a[i] == b:
            return True
        i += 1
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
    

# max fn 


if __name__ == "__main__":
    main()
