#!/usr/bin/env python3
"""Module définissant la classe Rectangle, héritant de BaseGeometry."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Représente un rectangle utilisant BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialise un nouveau Rectangle.

        Args:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            int: La surface du rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Retourne la représentation sous forme de chaîne du rectangle.

        Returns:
            str: Description du rectangle au format [Rectangle] width/height.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
