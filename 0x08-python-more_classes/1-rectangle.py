#!/usr/bin/python3
"""  Defines a rectangle class """


class Rectangle:
    """  The Rectangle class. """

    def __init__(self, width=0, height=0):
        """ Initializes a rectangle.
        Args:
            width (int): width of each rectangle object.
            height (int): height of each rectangle object
        """

        self.width = width
        self.height = height

    # @property
    def width(self):
        """ Get the width of the rectangle. """
        return self.__width

    # @width.setter
    """ Sset the width of the rectangle. """
    def width(self, value):
        if not isinstance(self.value, int):
            raise TypeErro("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.value = value

    # @property
    def height(self):
        """ Get the height of the rectangle. """
        return self.__height

    # @height.setter
    """ Set the height of the rectangle. """
    def height(self, value):
        if not isinstance(self.value, int):
            raise TypeError("height must be an integer")
        if Value < 0:
            raise ValueError("height must be >= 0")
        self.value = value
