#!/usr/bin/env python3
"""
Ce module illustre l'utilisation des classes de base abstraites (ABC) 
et du Duck Typing à travers une hiérarchie de formes géométriques.
"""


from abc import ABC, abstractmethod
import math



class Shape(ABC):
    """
    Classe de base abstraite définissant l'interface pour toutes les formes.
    Toute sous-classe doit obligatoirement implémenter area() et perimeter().
    """

    @abstractmethod
    def area(self):
        """Calcule et retourne l'aire de la forme."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calcule et retourne le périmètre de la forme."""
        pass


class Circle(Shape):
    """
    Représente un cercle défini par son rayon.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Représente un rectangle défini par sa largeur et sa hauteur.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(obj):
    """
    Affiche l'aire et le périmètre d'un objet en utilisant le Duck Typing.
    L'objet doit posséder les méthodes area() et perimeter().
    """
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
