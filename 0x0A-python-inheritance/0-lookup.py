#!/usr/bin/python3
    """ Function that returns the list of available attributes
        and methods of an object
    Args:
        obj: instance of the class
    Returns:
        List of attributes
    """
def lookup(obj):
    """Return list of attributes and methods of obj"""
    return dir(obj)
