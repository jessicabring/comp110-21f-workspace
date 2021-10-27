"""Counting letters in a string."""

<<<<<<< HEAD
__author__ = "730394024"
=======
__author__ = "730243388"
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1

letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
i: int = 0 
alpha_counter: int = 0

<<<<<<< HEAD
while i < len(word):
    if word[i] == letter:
        alpha_counter = alpha_counter + 1
    i = i + 1 

print("Count: " + str(alpha_counter))
=======
# Begin your solution here...

letter: str = input("What letter do you want to seach for? ")
word: str = input("Enter a word ")
count: int = 0
i: int = 0
while (i < len(word)):
    if word[i] == letter:
        count += 1
    i += 1
print("Count: " + str(count))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
