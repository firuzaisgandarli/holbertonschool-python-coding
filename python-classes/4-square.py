#!/usr/bin/python3
"""Square class with size validation, area method, and print method"""


class Square:
    """Defines a square by size"""

    def __init__(self, size=0):
        """Initialize a square with optional size"""
        self.size = size  # setter vasitəsilə validasiya

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
