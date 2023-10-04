#!/usr/bin/python3
""" The descrbes the class rectangle"""


class Rectangle:
    """ Contains the class definition"""

    def __init__(self, width=0, heigth=0):
        """Instantiation with optional width and height: def __init__(self, width=0, height=0):"""
        self.width = width
        self.heigth = heigth

    @property
    def width(self):
        """property def width(self): and retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def heigth(self):
        """property def heigth(self): and retrieve it"""
        return self.__heigth

    @heigth.setter
    def heigth(self, value):
        """property setter"""
        self.__heigth = value
        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")
        elif value < 0:
            raise ValueError("heigth must be >= 0")
