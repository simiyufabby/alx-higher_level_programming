#!/usr/bin/python3
"""
This is a module docstring. This module defines a Square class.
"""


class Square:
    """
    This class defines a square by size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        This method initializes the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        This method retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This method sets the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        This method retrieves the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This method sets the position of the square.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 +ive integers")

        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a tuple of 2 +ive integers")

        self.__position = value

    def area(self):
        """
        This method calculates the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        This method prints the square with the character #.
        """

        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)

    def __str__(self):

        if self.__size == 0:
            return ""

        result = "\n" * self.__position[1]

        for _ in range(self.__size):
            result += ' ' * self.__position[0] + '#' * self.__size + "\n"

        return result[:-1]
