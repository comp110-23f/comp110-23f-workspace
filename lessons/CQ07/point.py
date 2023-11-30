"""CQ07 OOP!"""
from __future__ import annotations

__author__ = "730664874"


class Point:
    """The Point class!"""
    x: float
    y: float

    def __init__(self, inp_x: float = 0.0, inp_y: float = 0.0):
        """Initializes x and y."""
        self.x = inp_x
        self.y = inp_y

    def scale_by(self, factor: int) -> None:
        """Scales x and y by a factor. Mutates the object it's called upon."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Scales x and y by a factor. Does not mutate the object it's called upon."""
        new_x: float = self.x * factor
        new_y: float = self.y * factor
        return Point(new_x, new_y)
    
    def __str__(self) -> str:
        """Returns prettier string for object output."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, other: int | float) -> Point:
        """Creates a new object multiplied by a factor."""
        return Point(self.x * other, self.y * other)

    def __add__(self, other: int | float) -> Point:
        """Creates a new object multiplied by a factor."""
        return Point(self.x + other, self.y + other)
    
