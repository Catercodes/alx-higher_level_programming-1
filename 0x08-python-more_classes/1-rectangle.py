#!/usr/bin/python3
""" Contain the class rectangle"""


class Rectangle:
    """ Definition class rectangle """

    def __init__(self, width=0, height=0):
        """Instantiaition with optional width and height """
        self.width = width
        self.height = height

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
        """set the value of the heigth"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
