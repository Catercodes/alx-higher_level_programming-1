#!/usr/bin/python3
""" Definition of a class"""


class Square:
    """An empty class that define a square"""

    def __init__(self, size=0):
        """private instance attribute: size"""
        self.__size = size

    @property
    def size(self):
        """property def size(self): to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter def size(self, value): to set it"""
        self.__size = value
        if not isinstance(value, int):
            """ raising errors """
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """returns the area of square"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print(self.__size * '#')
