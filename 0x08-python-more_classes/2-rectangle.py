#!/usr/bin/python3
"""Module containing Rectangle class"""


class Rectangle:
    """Class to create a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle with `width` and `height`.
        Args:
            width (int): width of rectangle with value >= 0.
            height (int): height of rectangle with value >= 0.
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """Getter to return value of 'height'.
        Returns: value of `height`.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter to define value for 'height'.
        Args:
            value (int): value to use for `height`.
        Raises:
            TypeError: If `value` is not of type int.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """Getter to return value of 'width'.
        Returns: value of `width`.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter to define value for 'width'.
        Args:
            value (int): value to use for `width`.
        Raises:
            TypeError: If `value` is not of type int.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """Method to calculate area of Rectangle instance"""
        return self.width * self.height

    def perimeter(self):
        """Method to calculate perimeter length of Rectangle instance.
        Returns: 2 * ('width' + 'height') if both `width` and `height` > 0, else 0.
        """
        return 2*(self.width + self.height) * bool(self.width and self.height)
