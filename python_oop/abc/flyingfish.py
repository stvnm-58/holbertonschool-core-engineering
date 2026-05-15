#!/usr/bin/env python3
"""
Module démontrant l'héritage multiple et l'ordre de résolution des méthodes (MRO).

Ce script définit une hiérarchie où une classe enfant (FlyingFish) combine 
les comportements de deux classes parentes (Fish et Bird).
"""


class Fish:
    """Représente un animal aquatique."""

    def swim(self):
        """Affiche le comportement de nage du poisson."""
        print("The fish is swimming")

    def habitat(self):
        """Affiche l'habitat naturel du poisson."""
        print("The fish lives in water")


class Bird:
    """Représente un animal aérien."""

    def fly(self):
        """Affiche le comportement de vol de l'oiseau."""
        print("the bird is flying")

    def habitat(self):
        """Affiche l'habitat naturel de l'oiseau."""
        print("The bird Lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Représente un poisson volant héritant de Fish et Bird.
    
    L'ordre des parents (Fish, Bird) détermine la priorité dans le MRO.
    """

    def fly(self):
        """Redéfinit le vol pour le poisson volant."""
        print("the flying fish is soaring!")

    def swim(self):
        """Redéfinit la nage pour le poisson volant."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Redéfinit l'habitat pour englober l'eau et le ciel."""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    # Instanciation de l'objet
    flying_fish = FlyingFish()

    # Appel des méthodes redéfinies
    flying_fish.fly()
    flying_fish.swim()
    flying_fish.habitat()

    # Affichage du Method Resolution Order (MRO)
    # On utilise les parenthèses car mro() est une méthode
    print("\nMethod Resolution Order:")
    print(FlyingFish.mro())
