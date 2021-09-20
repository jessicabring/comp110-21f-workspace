"""This is a quiz game to try to figure out the users' sign."""
from random import randint
player: str = ""
points: int
MAGIC: str = "\U0001F52E\U0001F4DC"
ARIES: str = "\U00002648"
TAURUS: str = "\U00002649"
GEMINI: str = "\U0000264A"
CANCER: str = "\U0000264B"
LEO: str = "\U0000264C"
VIRGO: str = "\U0000264D"
LIBRA: str = "\U0000264E"
SCORPIO: str = "\U0000264F"
SAGITTARIUS: str = "\U00002650"
CAPRICORN: str = "\U00002651"
AQUARIUS: str = "\U00002652"
PISCES: str = "\U00002653"
ALL_SIGNS: str = "\U00002648 \U00002649 \U0000264A \U0000264B \U0000264C \U0000264D \U0000264E \U0000264F \U00002650 \U00002651 \U00002652 \U00002653"
MEANIE: str = "\U0001F644\U0001F621"
HAPPY: str = "\U0001F601\U0001F60E\U0001F48B"


def greet() -> None:
    global player
    print(f"{MAGIC} Welcome to the Zodiac Guesser {MAGIC}")
    print(ALL_SIGNS)
    player = str(input("What is your earthly name? "))


def main() -> None:  
    global points
    points = 0
    i: int = 0
    greet()
    pretest()

    while i < 5:
        print(f"Points: {points}")
        game_loop: str = str(input("Do you wish to continue? (Y/N) \n"))
        if game_loop == "N":
            print(f"{MAGIC} GAME OVER {MAGIC}")
            exit()
        else:
            points = quiz(i, points)
        i = i + 1
    else: 
        final_result()


def pretest() -> None:
    global points
    knowledge: str = input(f"Hello, {player}! Do you have any prior knowledge about your {MAGIC} zodiac sign {MAGIC}? (Y/N) \n")
    if knowledge == "Y":
        points = points + 1
    if knowledge == "N":
        points = points - 1


def quiz(x: int, a: int) -> int:
    quiz_input: str
    if x == 0:
        quiz_input = input(f"{ALL_SIGNS} \n {player}, Are you: \n A. Introverted \n B. Extroverted \n C. Ambiverted \n D. I don't like people \n")
        a = algorithm(quiz_input)
        return a
    if x == 1:
        quiz_input = input(f"{ALL_SIGNS} \n A friend is talking about you behind your back. Do you: \n A. Find them and talk about it \n B. Ignore it because you're better than them \n C. Put a hex on them \n D. I talk to no one \n")
        a = algorithm(quiz_input)
        return a
    if x == 2:
        quiz_input = input(f"{ALL_SIGNS} \n Which word best describes you, {player}? \n A. Practical \n B. Awe-inspiring \n C. Odd \n D. Mysterious \n")
        a = algorithm(quiz_input)
        return a
    if x == 3: 
        quiz_input = input(f"{ALL_SIGNS} \n How many times a day do you think about yourself? \n A. I'm too busy \n B. Constantly \n C. Thrice \n D. I'm not telling you {MEANIE} \n")
        a = algorithm(quiz_input)
        return a
    if x == 4: 
        quiz_input = input(f"{ALL_SIGNS} \n What is your favorite color? \n A. Pink \n B. It changes every week \n C. You wouldn't know it \n D. Black \n")
        a = algorithm(quiz_input)
        return a
    return a


def algorithm(x: str) -> int:
    global points
    if x == "A":
        points = points + 1
    if x == "B":
        points = points + 2
    if x == "C":
        points = points + 3
    if x == "D":
        points = points + 4
    return points


def final_result() -> None:
    global points
    i: int = 0
    u: int = 0
    if points <= 6:
        print(f"{MAGIC} {player}, You are: {sign_gen(randint(1,3))} {MAGIC}")
    else:
        if points <= 11: 
            print(f"{MAGIC} {player}, You are: {sign_gen(randint(4,6))} {MAGIC}")
        else:
            if points <= 16:
                print(f"{MAGIC} {player}, You are: {sign_gen(randint(7,9))} {MAGIC}")
            else: 
                if points <= 21:
                    print(f"{MAGIC} {player}, You are: {sign_gen(randint(10,12))} {MAGIC}")
    while i < 1:
        feedback: str = input("Did I get it right? (Y/N) \n")
        if feedback == "N":
            try_again: str = input("Should I try again? (Y/N) \n")
            u = u + 1
            if try_again == "Y":
                if u <= 12: 
                    print(f"Maybe you are {sign_gen(u)}?")
            i = 0
            if try_again == "N":
                print(f"You must be a Scorpio {MEANIE} \n GAME OVER!")
                i = i + 1
        if feedback == "Y":
            print(f"{HAPPY} YAY!! {HAPPY} \n {MAGIC} GAME OVER {MAGIC}")
            i = i + 1


def sign_gen(x: int) -> str:
    if x == 1:
        return f"a Pisces {PISCES}!"
    if x == 2:
        return f"a Sagittarius {SAGITTARIUS}!"
    if x == 3:
        return f"a Capricorn {CAPRICORN}!"
    if x == 4: 
        return f"a Leo {LEO}!"
    if x == 5:
        return f"a Virgo {VIRGO}!"
    if x == 6:
        return f"a Libra {LIBRA}!"
    if x == 7:
        return f"an Aquarius {AQUARIUS}!"
    if x == 8: 
        return f"a Cancer {CANCER}!"
    if x == 9:
        return f"a Gemini {GEMINI}!"
    if x == 10:
        return f"a Scorpio {SCORPIO}!"
    if x == 11: 
        return f"an Aries {ARIES}!"
    else:
        return f"a Taurus {TAURUS}!"


if __name__ == "__main__":
    main()