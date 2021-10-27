<<<<<<< HEAD
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
=======
"""Demonstrates python numeric operators for two input numbers."""

__author__ = "730243388"

string_one = input("Left-hand side: ")
string_two = input("Right-hand side: ")

number_one = int(string_one)
number_two = int(string_two)

print(string_one + " ** " + string_two + " is " + str(number_one ** number_two))
print(string_one + " / " + string_two + " is " + str(number_one / number_two))
print(string_one + " // " + string_two + " is " + str(number_one // number_two))
print(string_one + " % " + string_two + " is " + str(number_one % number_two))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
