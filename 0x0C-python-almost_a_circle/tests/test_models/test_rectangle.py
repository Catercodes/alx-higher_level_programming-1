#!/usr/bin/python3
""" Rectangle Testcases"""
import unittest
import os
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """ Testcase to test  the rectangle class"""


    def test_inheritance(self):
        r1 = Rectangle(10, 2)
        self.assertTrue(isinstance(r1, Rectangle))
        self.assertTrue(isinstance(r1, Base))


    def test_getter_and_setter(self):
        r1 = Rectangle(1, 2, 3, 4)
        """ Testcases for setter """
        # Testing the setter and  getter for width
        self.assertEqual(r1.width, 1)
        r1.width = 8
        self.assertEqual(r1.width, 8)
        # Testing the setter and getter for height
        self.assertEqual(r1.height, 2)
        r1.height = 5
        self.assertEqual(r1.height, 5)
        # Testing the setter and getter for x
        r1.x = 3
        self.assertEqual(r1.x, 3)
        r1.x = 7
        self.assertEqual(r1.x, 7)
        with self.assertRaises(ValueError):
            r1.x = -4
        # Testing  the setter and getter for y
        r1.y = 4
        self.assertEqual(r1.y, 4)
        r1.y = 6
        self.assertEqual(r1.y, 6)
        with self.assertRaises(ValueError):
            r1.y = -4

    def test_constructor(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        """Testcase for Constructors"""
        # Testing the constructor
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 12)
