#!/usr/bin/python3
''' Defines a rectangle class '''


class Rectangle:
    ''' Iniializes two instance attributes
        @width and @height'''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def width(self):
        return self.__width

    def width(self, value):
        if not isinstance(self.value, int):
            raise TypeErro("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.value = value

    def height(self):
        return self.__height

    def height(self, value):
        if not isinstance(self.value, int):
            raise TypeError("height must be an integer")
        if Value < 0:
            raise ValueError("height must be >= 0")
        self.value = value
