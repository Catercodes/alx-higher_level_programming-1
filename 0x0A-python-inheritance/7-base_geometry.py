#!/usr/bin/python3
"""Contains class BaseGeometry"""


class BaseGeometry:
    """Non Empty BaseGeometry class"""

    def area(self):
        """area method to not be implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if not isinstance(value, int):
            """raising exceptions"""
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
