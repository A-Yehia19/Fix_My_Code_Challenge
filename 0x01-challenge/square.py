#!/usr/bin/python3

"""
Square class
"""


class square():
    """ Documentation """
    __width = 0
    __height = 0

    def __init__(self, width = 0, height = 0):
        """ Constructor """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter """
        return self.__width
    
    @width.setter
    def width(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """ Getter """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Permiter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation of the square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
