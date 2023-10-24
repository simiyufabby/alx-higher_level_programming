#!/usr/bin/python3

class Square:
    '''
    This is a class that defines a square.
    '''
    def __init__(self, size=0):
        '''
        Initialize Square instance with size.
        '''
        self.size = size

    @property
    def size(self):
        '''
        Getter for size.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Setter for size.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''
        Returns the current square area.
        '''
        return self.__size ** 2
