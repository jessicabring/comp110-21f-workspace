"""Finding duplicate letters in a word."""

__author__ = "730394024"

result: bool


def duplicates(a: str) -> bool:
    """Returns a bool value determining whether the string input contains duplicate letters."""
    i: int = 0
    j: int = 1

    while i < len(a):
        j = i + 1
        while j < len(a):
            if a[i] == a[j]:
                result = True 
                return result
            j = j + 1
        i = i + 1
    else:
        result = False
        return result


output: bool = duplicates(str(input("Enter a word: ")))
print("Found duplicate: " + str(output))
