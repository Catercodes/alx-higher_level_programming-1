#!/usr/bin/python3
"""Contains function read_file"""


def append_write(filename="", text=""):
    """Write a function that appends a string at the end of a text
    file (UTF8) and returns the number of characters added"""
    with open(filename, mode='a', encoding="utf-8") as a_file:
        data = a_file.write(text)
        return data
