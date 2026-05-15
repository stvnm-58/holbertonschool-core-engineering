#!/usr/bin/env python3
"""Module définissant une structure de base pour des animaux et leurs cris."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Classe de base abstraite représentant un animal."""

    @abstractmethod
    def sound(self):
        """Retourne le cri spécifique de l'animal.

        Cette méthode doit être implémentée par toutes les sous-classes.
        """
        pass


class Dog(Animal):
    """Classe représentant un chien."""

    def sound(self):
        """Retourne le cri du chien."""
        return "Bark"


class Cat(Animal):
    """Classe représentant un chat."""

    def sound(self):
        """Retourne le cri du chat."""
        return "Meow"