#!/usr/bin/python3
"""Contain Class """
from models.base import Base


class Rectangle(Base):
    """ inherit from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Private class constructors"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ retrive the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting value"""
        self.validate_value(value, 'width')
        self.__width = value

    @property
    def height(self):
        """ retrive the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting value"""
        self.validate_value(value, 'height')
        self.__height = value

    @property
    def x(self):
        """ retrive the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting value"""
        self.validate_value(value, 'x')
        self.__x = value

    @property
    def y(self):
        """ retrive the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting value"""
        self.validate_value(value, 'y')
        self.__y = value

    def validate_value(self, value, attr):
        """ Validate Value"""
        if not isinstance(value, int):
            raise TypeError(f"{attr} must be an integer")
        if attr == 'x' or attr == 'y':
            if value < 0:
                raise ValueError(f"{attr} must be >= 0")
        elif value <= 0:
            raise ValueError(f"{attr} must be > 0")

    def area(self):
        """ return the value of area of the rectangle """
        return self.__width * self.__height
