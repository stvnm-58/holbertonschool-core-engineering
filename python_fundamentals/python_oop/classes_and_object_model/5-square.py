#!/usr/bin/env python3
"""
Ce module définit la classe Square.
"""


class Square:
    """
    Représente un carré.
    """

    def __init__(self, size=0):
        """
        Initialise une nouvelle instance de Square.

        Args:
            size (int): La taille du côté du carré.
        """
        self.size = size

    @property
    def size(self):
        """
        Récupère la taille du carré.

        Returns:
            int: La taille du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Définit la taille du carré.

        Args:
            value (int): La nouvelle taille.

        Raises:
            TypeError: Si la valeur n'est pas un entier.
            ValueError: Si la valeur est inférieure à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcule l'aire du carré.

        Returns:
            int: L'aire du carré.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Affiche le carré dans la console en utilisant le caractère #.
        Si la taille est 0, affiche une ligne vide.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)
