"""Program that outputs one of at least four random, good fortunes."""

<<<<<<< HEAD
__author__ = "730394024"
=======
__author__ = "730243388"
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1

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

<<<<<<< HEAD
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
=======
# Begin your solution here...

rand_int: int = randint(0, 3)
print("Your fortune cookie says...")
if (rand_int == 0):
    print("you will get married")
elif (rand_int == 1):
    print("you should take a nap")
elif (rand_int == 2):
    print("you need therapy")
else:
    print("you will meet a new friend tommorow")
print("Now, go spread positive vibes!")
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
