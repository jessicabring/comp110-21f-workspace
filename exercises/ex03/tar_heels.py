"""An exercise in remainders and boolean logic."""

__author__ = "730394024"

user_word: str


def carolina_word(a: int) -> str:
    """Returns a UNC related phrase depending on the divisibility of the user input by 7 and or 2."""  
    if a % 2 == 0:
        user_word = "TAR"
        if a % 7 == 0:
            user_word = "TAR HEELS"
    else: 
        if a % 7 == 0:
            user_word = "HEELS"
        else:
            user_word = "CAROLINA"
    return user_word


output: str = carolina_word(int(input("Enter an int: ")))
print(output)