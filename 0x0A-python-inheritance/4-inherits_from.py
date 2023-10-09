#!/usr/bin/python3
""" Am tired """


def inherits_from(obj, a_class):
    """Write a function that returns True if the object is an instance of a
    class that inherited (directly or indirectly)
    from the specified class ; otherwise False."""
    if isinstance(obj, a_class):
        return False
    return isinstance(obj, a_class)
