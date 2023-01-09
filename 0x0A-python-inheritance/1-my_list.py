#!/usr/bin/python3
"""Module implementing MyList class"""

class MyList(list):
    def print_sorted(self):
        """Prints the list in a sorted order"""
        print(sorted(self))
