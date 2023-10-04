#!/usr/bin/python3
""" Contain the class rectangle"""


class Rectangle:
    """ Definition class rectangle """

    def __init__(self, width=0, heigth=0):
        """Instantiaition with optional width and height """
        self.width = width
        self.heigth = heigth

    @property
    def width(self):
        """retrieves width   of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of the width"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def heigth(self):
        """retrieve the lenght of the heigth of the rectangle"""
        return self.__heigth

    @heigth.setter
    def heigth(self, value):
        """set the value of the heigth"""
        self.__heigth = value
        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")
        elif value < 0:
            raise ValueError("heigth must be >= 0")
