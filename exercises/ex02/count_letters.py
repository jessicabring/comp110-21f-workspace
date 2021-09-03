"""Counting letters in a string."""

__author__ = "730394024"

letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
i: int = 0 
alpha_counter: int = 0

while i < len(word):
    if word[i] == letter:
        alpha_counter = alpha_counter + 1
    i = i + 1 

print("Count: " + str(alpha_counter))
