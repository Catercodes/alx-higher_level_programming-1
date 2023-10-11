#!/usr/bin/python3
"""function that create an Object to a text file"""
import json


def load_from_json_file(filename):
    """funtion that create json file"""
    with open(filename, mode='r', encoding="utf-8") as a_file:
        data = a_file.read()
        return json.loads(data)
