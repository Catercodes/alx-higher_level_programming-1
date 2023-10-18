#!/usr/bin/python3
""" Contain The Rectangle """
from models.base import Base


class Rectangle(Base):
    """
    Subclass of Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Private instance attributes, each with its own public
        getter and setter"""
        Base.__init__(self, id)
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    @property
    def width(self):
        """ public getter and setter also retrieve it """
        return self._width

    @width.setter
    def width(self, value):
        """ raising exceptions"""
        self.validate_int('width', value)
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
        """raising Exceptions"""
        self.validate_int('height', value)
        if not isinstance(value, int):
            raise TypeError(f"{height} must be an integer")
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
        self.validate_int('x', value)
        if not isinstance(value, int):
            raise TypeError(f"{x} must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self._x = value

    @property
    def y(self):
        """ public getter and setter"""
        return self._y

    @y.setter
    def y(self, value):
        """ raise exceptions"""
        self.validate_int('y', value)
        if not isinstance(value, int):
            raise TypeError("{} must be an integer")
        if value < 0:
            raise ValueError("{} must be > 0")
        self._y = value

    def validate_int(self, name, value):
        """Validates value is an integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if name == 'x' or name == 'y':
            if value < 0:
                raise ValueError(f"{name} must be >= 0")
        else:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
