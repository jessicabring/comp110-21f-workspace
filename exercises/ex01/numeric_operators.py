"""A program that allows the user to understand how numerical operators work in python."""

__author__ = "730394024"

left_number: int = int(input("Left-hand side: "))
right_number: int = int(input("Right-hand side: "))

exponentiation: int = left_number ** right_number 
division: float = left_number / right_number
integer_division: int = left_number // right_number
remainder_division: int = left_number % right_number

print(str(left_number) + " ** " + str(right_number) + " is " + str(exponentiation))
print(str(left_number) + " / " + str(right_number) + " is " + str(division))
print(str(left_number) + " // " + str(right_number) + " is " + str(integer_division))
print(str(left_number) + " % " + str(right_number) + " is " + str(remainder_division))