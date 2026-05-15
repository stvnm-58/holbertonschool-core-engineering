#!/usr/bin/env python3
"""
Module de gestion de formes géométriques.

Ce script utilise des classes de base abstraites (ABC) pour définir un contrat 
pour les formes et illustre le concept de Duck Typing.
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Classe de base abstraite définissant l'interface des formes."""

    @abstractmethod
    def area(self):
        """
        Calcule l'aire de la forme.

        Returns:
            float: L'aire calculée.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calcule le périmètre de la forme.

        Returns:
            float: Le périmètre calculé.
        """
        pass


class Circle(Shape):
    """Représente un cercle géométrique."""

    def __init__(self, radius):
        """
        Initialise le cercle.

        Args:
            radius (float): Le rayon du cercle.
        """
        self.radius = radius

    def area(self):
        """
        Calcule l'aire du cercle.

        Returns:
            float: Aire calculée via pi * r^2.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calcule le périmètre du cercle.

        Returns:
            float: Périmètre calculé via 2 * pi * r.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Représente un rectangle géométrique."""

    def __init__(self, width, height):
        """
        Initialise le rectangle.

        Args:
            width (float): La largeur du rectangle.
            height (float): La hauteur du rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            float: Aire calculée via largeur * hauteur.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
            float: Périmètre calculé via 2 * (largeur + hauteur).
        """
        return 2 * (self.width + self.height)


def shape_info(obj):
    """
    Affiche les informations d'une forme via Duck Typing.

    Args:
        obj (Shape): Un objet qui doit posséder les méthodes area() et perimeter().
    """
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
