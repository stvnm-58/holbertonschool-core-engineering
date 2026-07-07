#!/usr/bin/env python3
"""
Ce module contient une fonction qui lit un fichier texte.
"""


def read_file(filename=""):
    """Lit un fichier texte (UTF8) et l'imprime dans stdout."""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
