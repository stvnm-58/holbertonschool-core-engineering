#!/usr/bin/env python3
"""Module de gestion de formes géométriques via ABC et Duck Typing."""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Classe de base abstraite définissant l'interface des formes."""

    @abstractmethod
    def area(self):
        """Calcule l'aire."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calcule le périmètre."""
        pass


class Circle(Shape):
    """Représente un cercle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Représente un rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Affiche les informations d'une forme."""
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
