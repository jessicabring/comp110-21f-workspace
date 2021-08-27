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