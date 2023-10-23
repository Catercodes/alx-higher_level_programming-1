#!/usr/bin/python3
""" Contain the class rectangle"""


class Rectangle:
    """ Definition class rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiaition with optional width and height """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieves width   of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the lenght of the heigth of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the rectangle area"""
        return self.height * self.width

    def perimeter(self):
        """return the primeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """ return the rectangle with the character #:"""
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)

        row = symbol * self.__width + "\n"
        rectangle = row * (self.__height - 1) + (self.__width * symbol)
        return rectangle

    def __repr__(self):
        """ return the string representation of thr rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """return amessage good bye when the intance is delected"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
