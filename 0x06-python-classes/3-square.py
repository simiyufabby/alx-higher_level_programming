#!/usr/bin/python3
"""
This module defines a Square class.
Its purpose is to define a square with a certain size.
"""


class Square:
    """
    This is a Square class.
    It defines a square of a given size, with size being an optional parameter.
    """

    def __init__(self, size=0):
        """
        This is the constructor method for Square.
        It initializes a Square instance with a given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        This method returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
