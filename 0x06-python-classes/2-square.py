#!/usr/bin/python3
""" Definition of a class"""


class Square:
    """An empty class that define a square"""
    def __init__(self, size=0):
        """private instance attribute: size"""
        self.__size = size
        if not isinstance(size, int):
            """ raising errors """
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
