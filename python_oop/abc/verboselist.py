#!/usr/bin/env python3
"""Module définissant VerboseList, une liste qui notifie ses modifications."""


class VerboseList(list):
    """Liste personnalisée qui affiche un message à chaque modification."""

    def append(self, item):
        """Ajoute un élément à la fin de la liste et l'annonce.

        Args:
            item: L'élément à ajouter.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Étend la liste avec un itérable et annonce le nombre d'éléments.

        Args:
            iterable: L'itérable dont les éléments seront ajoutés.
        """
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Retire la première occurrence de l'élément et l'annonce.

        Args:
            item: L'élément à retirer.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Retire et retourne l'élément à la position donnée en l'annonçant.

        Args:
            index: L'index de l'élément à retirer (-1 par défaut).

        Returns:
            L'élément retiré.
        """
        print("Popped [{}] from the list.".format(self[index]))
        return super().pop(index)
