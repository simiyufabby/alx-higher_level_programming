#!/usr/bin/python3

class Square:
    '''
    This is a class that defines a square.
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''
        Initialize Square instance with size and position.
        '''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''
        Getter for position.
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        Setter for position.
        '''
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        '''
        Returns the current square area.
        '''
        return self.__size ** 2

    def my_print(self):
        '''
        Prints the square with the character #.
        If size is equal to 0, print an empty line.
        Position should be used by using space.
        Don't fill lines by spaces when position[1] > 0.
        '''
        if self.__size == 0:
            print()
            return

        print('\n' * self.__position[1], end='')

        for _ in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)
