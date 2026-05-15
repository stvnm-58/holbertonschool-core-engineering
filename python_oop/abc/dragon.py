#!/usr/bin/env python3
"""
Module defining mixins and a Dragon class using multiple inheritance.
"""


class SwimMixin:
    """
    Mixin that provides swimming capability.
    """

    def swim(self):
        """
        Print swimming behavior.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin that provides flying capability.
    """

    def fly(self):
        """
        Print flying behavior.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that can swim, fly, and roar.
    """

    def roar(self):
        """
        Print roaring behavior.
        """
        print("The dragon roars!")


if __name__ == "__main__":
    dragon = Dragon()
    dragon.swim()
    dragon.fly()
    dragon.roar()
