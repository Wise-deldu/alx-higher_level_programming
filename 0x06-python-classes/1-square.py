#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Empty class with size private attribute
    """
    def __init__(self, size):
        """Initialize a new Square
        Args:
            size (int): size of the square
        """
        self.__size = size
