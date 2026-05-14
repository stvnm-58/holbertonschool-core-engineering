#!/usr/bin/env python3
"""Module définissant la classe BaseGeometry."""


class BaseGeometry:
    """Classe de base pour les opérations géométriques."""

    def area(self):
        """
        Lève une exception car la méthode n'est pas implémentée.

        Raises:
            Exception: Toujours levée.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide si la valeur est un entier strictement supérieur à 0.

        Args:
            name (str): Nom de la variable.
            value (int): Valeur à vérifier.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur ou égal à 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))