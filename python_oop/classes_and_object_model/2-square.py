#!/usr/bin/env python3
"""
Module 2-square
Defines a class Square with size validation.
"""


class Square:
    """
    Class Square that defines a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
