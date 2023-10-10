#!/usr/bin/python3
"""contains a function read a text"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, mode='r', encoding='utf-8') as a_file:
        for line in a_file:
            data = a_file.read()
            print(data, end="")
