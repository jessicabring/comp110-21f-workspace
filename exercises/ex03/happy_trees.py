"""Drawing forests in a loop."""

__author__ = "730394024"

# The string constant for the pine tree emoji
depth: int = int(input("Depth: "))
line: int = 1


def forest_maker(a: int) -> str:
    """Creates a row of trees by adding onto an existing string."""
    TREE: str = '\U0001F332'
    row: str = TREE
    i: int = 1

    while i < a:
        row = row + TREE
        i = i + 1
    return row


while line <= depth: 
    picture: str = forest_maker(line)
    line = line + 1
    print(picture)
