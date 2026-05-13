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
            size (int): La taille du côté du carré.

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur à 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calcule l'aire du carré.

        Returns:
            int: L'aire du carré (taille * taille).
        """
        return self.__size * self.__size
