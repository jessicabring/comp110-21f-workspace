"""Repeating a beat in a loop."""

__author__ = "730394024"


beat: str = input("What beat do you want to repeat? ")
number: int = int(input("How many times do you want to repeat it? "))
counter: int = 1
music: str = beat

while counter < number:
    music = music + " " + beat
    counter = counter + 1

if counter == number:
    print(music)
else:
    if number <= 0:
        print("No beat...")
