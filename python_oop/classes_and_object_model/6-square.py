#!/usr/bin/env python3
"""
Ce module définit la classe Square.
"""


class Square:
    """
    Représente un carré.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise une nouvelle instance de Square.

        Args:
            size (int): La taille du côté du carré.
            position (tuple): La position (x, y) du carré.
        """
        self.size = size
        self.position = position

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
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Récupère la position du carré.

        Returns:
            tuple: La position (x, y) du carré.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Définit la position du carré.

        Args:
            value (tuple): La nouvelle position.

        Raises:
            TypeError: Si value n'est pas un tuple de 2 entiers positifs.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """
        Calcule l'aire du carré.

        Returns:
            int: L'aire du carré.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Définit la représentation sous forme de chaîne de caractères du carré.

        Returns:
            str: Le carré représenté avec des # et tenant compte de la position.
        """
        if self.__size == 0:
            return ""

        res = []
        for _ in range(self.__position[1]):
            res.append("")

        for _ in range(self.__size):
            res.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(res)

    def my_print(self):
        """
        Affiche le carré dans la console.
        Si la taille est 0, affiche une ligne vide.
        """
        if self.__size == 0:
            print("")
        else:
            print(self)
