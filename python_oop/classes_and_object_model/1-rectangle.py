#!/usr/bin/env python3
"""
Ce module définit la classe Rectangle.
"""


class Rectangle:
    """
    Représente un rectangle avec une largeur et une hauteur.
    """

    def __init__(self, width=0, height=0):
        """
        Initialise une nouvelle instance de Rectangle.

        Args:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Récupère la largeur du rectangle.

        Returns:
            int: La largeur du rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Définit la largeur du rectangle.

        Args:
            value (int): La nouvelle largeur.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Récupère la hauteur du rectangle.

        Returns:
            int: La hauteur du rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Définit la hauteur du rectangle.

        Args:
            value (int): La nouvelle hauteur.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
