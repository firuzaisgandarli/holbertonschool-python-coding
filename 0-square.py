#!/usr/bin/python3
"""
This module defines the Square class, which represents a geometric square.
The class currently stores only the size as a private attribute.
"""


class Square:
    """
    Represents a square with a private size attribute.
    The size is stored privately to allow controlled access in future tasks.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with a given size.

        Args:
            size: The size of the square (no type/value validation required here).
        """
        self.__size = size
