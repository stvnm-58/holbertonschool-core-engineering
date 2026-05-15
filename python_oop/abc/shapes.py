#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Classe de base abstraite (ABC) servant de blueprint.
    Elle force les sous-classes à implémenter area et perimeter.
    """

    @abstractmethod
    def area(self):
        """Méthode abstraite pour l'aire."""
        pass

    @abstractmethod
    def perimeter(self):
        """Méthode abstraite pour le périmètre."""
        pass


class Circle(Shape):
    """Implémentation concrète pour un cercle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Implémentation concrète pour un rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(obj):
    """
    Fonction standalone utilisant le Duck Typing.
    Elle ne vérifie pas le type (pas de isinstance), elle appelle
    juste les méthodes dont elle a besoin.
    """
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
