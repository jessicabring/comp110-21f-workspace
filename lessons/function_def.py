"""An example function definition."""


def my_max(a: int, b: int) -> float:
    """Returns the largest argument."""
    if a >= b:
        return a
        
    return b


x: int = 6
y: int = 5 + 2
z: float = my_max(x, y)
print(z)
