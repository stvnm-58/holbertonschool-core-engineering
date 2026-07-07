#!/usr/bin/env python3
""" Ce module contient une fonction qui ecrit dans un fichier texte
"""


def write_file(filename="", text=""):
    """Ecrit dans le fichier texte (UTF8) et renvoie le nombre de caractères"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
