#!/usr/bin/env python3
"""
Module illustrant l'usage des Mixins pour composer des comportements.
"""


class SwimMixin:
    """Mixin fournissant la capacité de nager."""

    def swim(self):
        """Affiche un message de nage."""
        print("the creature swims!")


class FlyMixin:
    """Mixin fournissant la capacité de voler."""

    def fly(self):
        """Affiche un message de vol."""
        print("The creature Flies!")


class Dragon(FlyMixin, SwimMixin):
    """
    Un dragon qui combine les capacités de vol et de nage via des Mixins.
    """

    def roar(self):
        """Affiche le rugissement spécifique du dragon."""
        print("The dragon roars!")


if __name__ == "__main__":
    # Création de l'instance
    # Note l'indentation de 4 espaces ici
    smaug = Dragon()

    # Démonstration des capacités
    smaug.swim()
    smaug.fly()
    smaug.roar()
