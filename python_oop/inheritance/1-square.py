#!/usr/bin/env python3
"""Module définissant la classe Square."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Square(BaseGeometry):
    """Représente un carré qui hérite de BaseGeometry."""

    def __init__(self, size):
        """
        Initialise un nouveau carré.

        Args:
            size (int): La taille du côté du carré.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Calcule la surface du carré.

        Returns:
            int: Le résultat de size multiplié par lui-même.
        """
        return self.__size * self.__size
