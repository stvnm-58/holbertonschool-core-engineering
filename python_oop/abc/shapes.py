#!/usr/bin/env python3
"""Module de gestion de formes géométriques via ABC et Duck Typing."""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Classe de base abstraite définissant l'interface des formes."""

    @abstractmethod
    def area(self):
        """Calcule et retourne l'aire de la forme."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calcule et retourne le périmètre de la forme."""
        pass


class Circle(Shape):
    """Représente un cercle calculé à partir de son rayon."""

    def __init__(self, radius):
        """Initialise le cercle avec un rayon spécifique."""
        self.radius = radius

    def area(self):
        """Retourne l'aire du cercle (pi * r^2)."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Retourne le périmètre du cercle (2 * pi * r)."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Représente un rectangle calculé à partir de sa largeur et hauteur."""

    def __init__(self, width, height):
        """Initialise le rectangle avec largeur et hauteur."""
        self.width = width
        self.height = height

    def area(self):
        """Retourne l'aire du rectangle (L * l)."""
        return self.width * self.height

    def perimeter(self):
        """Retourne le périmètre du rectangle (2 * (L + l))."""
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Affiche l'aire et le périmètre d'un objet via Duck Typing."""
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
