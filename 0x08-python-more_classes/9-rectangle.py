#!/usr/bin/python3
"""  Defines a rectangle class """


class Rectangle:
    """  The Rectangle class. """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initializes a rectangle.
        Args:
            width (int): width of each rectangle object.
            height (int): height of each rectangle object
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    # @property
    def width(self):
        """ Get the width of the rectangle. """
        return self.__width

    # @width.setter
    """ Sset the width of the rectangle. """
    def width(self, value):
        if not isinstance(value, int):
            raise TypeErro("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    # @property
    def height(self):
        """ Get the height of the rectangle. """
        return self.__height

    # @height.setter
    """ Set the height of the rectangle. """
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """  Returning area for the rectangle. """
        return self.width * self.height

    def perimeter(self):
        """ Returning the perimeter of the rectangle. """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """ String representation of the rectangle. """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return ('\n'.join([str(self.print_symbol) *
                    self.width] * self.height)
                    )

    def __repr__(self):
        """ returning a string representation of the rectangle
        to be able to recreate a new instance by using eval() """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
