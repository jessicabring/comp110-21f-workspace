"""An exercise in remainders and boolean logic."""

<<<<<<< HEAD
__author__ = "730394024"
=======
__author__ = "730243388"
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1

user_word: str

<<<<<<< HEAD

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
=======
# Begin your solution here...
num: int = int(input("Enter an int: "))

if (num % 14 == 0):
    print("TAR HEELS")
elif (num % 7 == 0):
    print("HEELS")
elif (num % 2 == 0):
    print("TAR")
else:
    print("CAROLINA")
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
