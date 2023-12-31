#!/usr/bin/python3
"""Contains class square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Subclass Square of parent class Rectangle"""
    def __init__(self, size):
        """Initializes the instance attributes"""
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size
