<<<<<<< HEAD
"""This program is intended to give me more practice with relational operators."""

__author__ = "730394024"

left_number: int = int(input("Left-hand side: "))
right_number: int = int(input("Right-hand side: "))

less_than: bool = left_number < right_number
greater_equal: bool = left_number >= right_number
equal_to: bool = left_number == right_number
not_equal: bool = left_number != right_number

print(str(left_number) + " < " + str(right_number) + " is " + str(less_than))
print(str(left_number) + " >= " + str(right_number) + " is " + str(greater_equal))
print(str(left_number) + " == " + str(right_number) + " is " + str(equal_to))
print(str(left_number) + " != " + str(right_number) + " is " + str(not_equal))
=======
"""Demonstrates python relational operators for two number inputs."""

__author__ = "730243388"

string_one = input("Left-hand side: ")
string_two = input("Right-hand side: ")

number_one = int(string_one)
number_two = int(string_two)

print(string_one + " < " + string_two + " is " + str(number_one < number_two))
print(string_one + " >= " + string_two + " is " + str(number_one >= number_two))
print(string_one + " == " + string_two + " is " + str(number_one == number_two))
print(string_one + " != " + string_two + " is " + str(number_one != number_two))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
