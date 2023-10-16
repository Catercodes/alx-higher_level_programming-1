#!/usr/bin/python3
from models.base import Base
""" contains The Rectangle """


class Rectangle(Base):
    """Class Rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Private instance attributes"""
        self._width = width
        self._height = height
        self._x = x
        self._y = y
        super().__init__(id)
        """Call the super class with id - this super call
        with use the logic of the __init__ of the Base class"""
    
    @property
    def width(self):
        """ public getter and setter"""
        return self._width

    @width.setter
    def width(self, value):
        """ raise exceptions"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer")
        if value <= 0:
            raise ValueError("width must be an integer")
        self._width = value

    @property
    def height(self):
        """ public getter and setter"""
        return self._height

    @height.setter
    def height(self, value):
        """public getter and setter"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer")
        if value <= 0:
            raise ValueError("heigth must be an integer")
        self._height = value

    @property
    def x(self):
        """ public getter and setter"""
        return self._x

    @x.setter
    def x(self, value):
        """raise exceptions"""
        if not isinstance(value, int):
            raise TypeError(" must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self._x = value

    @property
    def y(self):
        """ public getter and setter"""
        return self._x

    @y.setter
    def y(self, value):
        """ raise exceptions"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer")
        if value < 0:
            raise ValueError("{} must be > 0")
        self._y = value
