#!/usr/bin/python3

class square:
    def __init__(self, size=0):
        '''new square initialization
        args:
        size (int): the size of a new square
        '''
        if not isinstance(size, int):
            raise TypeError('Size must be an integer')
        elif size < 0:
            raise ValueError('Size must be >= 0')
        self.__size = size

    def area(self):
        '''' current area of the square'''
        return(self.__size * self.__size)
