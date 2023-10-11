#!/usr/bin/python3
""" Contain inherited class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Instantiation with width and height"""

        self.width = width
        self.height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
