#!/usr/bin/python3
"""Module containing Rectangle class"""


class Rectangle:
    """Class to create a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle with 'width' and 'height'.

        Args:
            width (int): width of rectangle with value >= 0.
            height (int): height of rectangle with value >= 0.
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """Getter that returns value of the height

        Returns: height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter that defines value of height

        Args:
            value (int): value to use for 'height'.

        Raises:
            TypeError: If 'value' is not of type int.
            ValueError: If 'value' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raises ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """Getter that returns value of the width

        Returns: width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter that defines value for width

        Args:
            value (int): value to use for 'width'.

        Raises:
            TypeError: If 'value' is not of type int.
            ValueError: If 'value' is less than 0/
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
