"""Example diagram problem."""

age: int = int(input("How old are you? "))
"""the int = int basically protects the variable from producing an error if its assigned a string value later on"""
year: int = int(input("What year is it? "))
age_in_2041: int = 2041 - year + age
print("In 2041, you'll be " + str(age_in_2041))

age = age + 1
year = year + 1
print("In " + str(year) + ", you'll be " + str(age))