#!/usr/bin/env python3
"""Module définissant la classe Square."""
Rectangle = __import__('Rectangle').Rectangle


class Square(rectangle):
    """Représente un carré qui hérite de BaseGeometry."""

    def __init__(self, size):
        """
        Initialise un nouveau carré.

        Args:
            size (int): La taille du côté du carré.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calcule la surface du carré.

        Returns:
            int: Le résultat de size multiplié par lui-même.
        """
        return self.__size * self.__size
