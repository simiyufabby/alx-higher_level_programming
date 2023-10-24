#!/usr/bin/python3
"""
This is a module docstring. This module defines a Square class.
"""


class Square:
    """
    This class defines a square by size.
    """

    def __init__(self, size=0):
        """
        This method initializes the square.
        """
        self.size = size

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
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        This method calculates the area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        This method checks if two squares are equal by area.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        This method checks if two squares are not equal by area.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        This method checks if one square is less than another by area.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Method checks if one square is less than or equal to another by area.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        This method checks if one square is greater than another by area.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if one square is greater than /equal to another by area.
        """
        return self.area() >= other.area()
