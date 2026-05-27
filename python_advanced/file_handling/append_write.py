#!/usr/bin/env python3
""" Ce module contient une fonction qui ajoute du texte à la fin d'un fichier
"""


def append_write(filename="", text=""):*
    """Ajoute une chaîne à la fin d'un fichier (UTF-8).
    Renvoie le nombre de caractères ajoutés.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
