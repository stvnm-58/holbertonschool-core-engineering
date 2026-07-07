#!/usr/bin/env python3
"""
Ce module définit des mixins pour la nage et le vol,
et les utilise pour créer une classe Dragon.
"""


class SwimMixin:
    """Mixin fournissant la capacité de nager."""
    def swim(self):
        """Affiche le comportement de nage."""
        print("The creature swims!")


class FlyMixin:
    """Mixin fournissant la capacité de voler."""
    def fly(self):
        """Affiche le comportement de vol."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Classe Dragon héritant des capacités de nage et de vol via des mixins.
    """
    def roar(self):
        """Affiche le rugissement du dragon."""
        print("The dragon roars!")
