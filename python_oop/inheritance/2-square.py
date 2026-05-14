#!/usr/bin/env python3
"""Module définissant la classe Square."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Représente un carré qui hérite de BaseGeometry."""

    def __init__(self, size):
        """
        Initialise un nouveau carré.

        Args:
            size (int): La taille du côté du carré.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calcule la surface du carré.

        Returns:
            int: Le résultat de size multiplié par lui-même.
        """
        return self.__size * self.__size

    def __str__(self):
        """Définit la représentation sous forme de chaîne de caractères.
        
        Returns:
            str: La description du carré au format [Square] <width>/<height>
        """
        # Comme on a passé size aux paramètres width et height du parent,
        # on peut réutiliser __size pour l'affichage.
        return "[Square] {}/{}".format(self.__size, self.__size)
