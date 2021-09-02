"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730394024"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

message: int = randint(1, 4)
print("Your fortune cookie says...")

if message == 1: 
    print("You will find success in your academic affairs.")
else:
    if message == 2:
        print("Tomorrow will bring good news.")
    else:
        if message == 3: 
            print("You will recieve communications from your soulmate today.")
        else: 
            print("22 will be your lucky number this week.")

print("Now, go spread positive vibes!")