#!/usr/bin/env python3
"""
Ce module définit la classe Square.
"""


class Square:
    """
    Représente un carré.
    """

    def __init__(self, size):
        """
        Initialise une nouvelle instance de Square.

        Args:
            size: La taille du côté du carré.
        """
        self.__size = size