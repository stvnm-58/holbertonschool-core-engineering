#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Classe de base abstraite représentant une forme géométrique."""

    @abstractmethod
    def area(self):
        """Calcule l'aire de la forme."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calcule le périmètre de la forme."""
        pass


class Circle(Shape):
    """Représentation d'un cercle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Représentation d'un rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


def shape_info(obj):
    """
    Affiche les informations d'une forme en utilisant le Duck Typing.
    Peu importe la classe de l'objet, tant qu'il a les méthodes requises.
    """
    print(f"Area : {obj.area()}")
    print(f"Perimeter : {obj.perimeter()}")
