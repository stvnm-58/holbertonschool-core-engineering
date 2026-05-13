#!/usr/bin/env python3
"""
Module 1-square
Définit une classe Square avec un attribut privé.
"""


class Square:
    """
    Classe Square qui définit un carré par sa taille.

    Attributes:
        __size (int): La taille d'un côté du carré (privée).
    """

    def __init__(self, size):
        """
        Initialise une nouvelle instance de Square.

        Args:
            size (int): La taille du côté du nouveau carré.
        """
        self.__size = size
