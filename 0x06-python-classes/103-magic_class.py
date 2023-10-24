#!/usr/bin/python3
"""
Module docstring:
This module defines a MagicClass that represents a circle.
"""

import math


class MagicClass:
    """
    Class docstring:
    This class defines a magic circle by radius.
    """

    def __init__(self, radius=0):
        """
        Method docstring:
        This method initializes the magic circle.
        Checks if the radius is a number int or float, else raises  TypeError.
        If the radius is less than 0, it raises a ValueError.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Method docstring:
        This method calculates and returns the area of the magic circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Method docstring:
        Calculates and returns the circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
