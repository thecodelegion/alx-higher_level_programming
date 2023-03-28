#!/usr/bin/python3

class square:
    
    def __init__(self, size=0):
        '''new square initialization
        args:
        size (int): the size of a new square
        '''
        if type(size) is int:
	    if size < 0:
	        raise ValueError('Size must be >= 0')
	    else:
                self.__size = size
	else:
	     raise TypeError('Size must be an integer')
