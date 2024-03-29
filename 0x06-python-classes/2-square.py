#!/usr/bin/python3

"""Define a class called Square"""


class Square:
    """Represent the Square"""

    def __init__(self, size=0):
        """Initialize a new Square

        Args:
            size: The size of a new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
