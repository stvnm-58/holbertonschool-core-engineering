#!/usr/bin/env python3
"""
Module 3-square
Définit une classe Square avec une méthode de calcul d'aire.
"""


class Square:
    """
    Classe Square qui définit un carré par sa taille.

    Attributes:
        __size (int): La taille d'un côté du carré (privée).
    """

    def __init__(self, size=0):
        """
        Initialise une nouvelle instance de Square.

        Args:
            size (int): La taille du côté du nouveau carré.

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
        Calcule l'aire du carré actuel.

        Returns:
            int: L'aire du carré (taille * taille).
        """
        return self.__size * self.__size
