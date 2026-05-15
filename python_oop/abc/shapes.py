#!/usr/bin/env python3
"""Module de calcul et d'affichage des propriétés géométriques de formes.

Ce script s'appuie sur une classe de base abstraite pour imposer une interface
commune à différentes formes géométriques et exploite le Duck Typing.
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Classe de base abstraite définissant l'interface commune des formes."""

    @abstractmethod
    def area(self):
        """Calcule l'aire de la forme.

        Returns:
            float: L'aire calculée.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Calcule le périmètre de la forme.

        Returns:
            float: Le périmètre calculé.
        """
        pass


class Circle(Shape):
    """Représente un cercle géométrique."""
    def __init__(self, radius):
        """Initialise le cercle avec son rayon.

        Args:
            radius (float): Le rayon du cercle.
        """
        self.radius = radius

    def area(self):
        """Calcule l'aire du cercle.

        Returns:
            float: Aire du cercle.
        """
        return math.pi * (self.radius**2)

    def perimeter(self):
        """Calcule le périmètre du cercle.

        Returns:
            float: Périmètre du cercle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Représente un rectangle géométrique."""
    def __init__(self, width, height):
        """Initialise le rectangle avec ses dimensions.

        Args:
            width (float): La largeur du rectangle.
            height (float): La hauteur du rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calcule l'aire du rectangle.

        Returns:
            float: Aire du rectangle (largeur * hauteur).
        """
        return self.width * self.height

    def perimeter(self):
        """Calcule le périmètre du rectangle.

        Returns:
            float: Périmètre du rectangle (2 * (largeur + hauteur)).
        """
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Affiche les informations d'une forme géométrique via Duck Typing.

    Args:
        obj (Shape): Un objet implémentant les méthodes area() et perimeter().
    """
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
