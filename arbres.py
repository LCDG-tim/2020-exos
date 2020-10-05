# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:39:48 2020

@author: Elève
"""


class ABR:
    def __init__(self, val):
        self.valeur = val
        self.gauche = None
        self.droit = None

    def inserer(self, x) -> None:
        if x < self.valeur:
            if self.gauche is not None:
                self.gauche.inserer(x)
            else:
                self.gauche = ABR(x)
        else:
            if self.droit is not None:
                self.droit.inserer(x)
            else:
                self.droit = ABR(x)

    def taille(self, arbre=None) -> int:
        if arbre is None:
            arbre = self
        if arbre.droit is None and arbre.gauche is None:
            return_val = 1

        elif arbre.droit is None and arbre.gauche is not None:
            return_val = 1 + self.taille(arbre.gauche)

        elif arbre.droit is not None and arbre.gauche is None:
            return_val = 1 + self.taille(arbre.droit)

        else:
            return_val = 1 + self.taille(arbre.gauche) \
                + self.taille(arbre.droit)

        return return_val

    def hauteur(self, arbre=None) -> int:
        if arbre is None:
            arbre = self

        r_is_none = arbre.droit is None
        l_is_none = arbre.gauche is None

        if r_is_none and l_is_none:
            return_val = 0

        elif not r_is_none and l_is_none:
            return_val = 1 + self.hauteur(arbre.droit)

        elif not l_is_none and r_is_none:
            return_val = 1 + self.hauteur(arbre.gauche)

        else:
            return_val = 1 + max(
                self.hauteur(arbre.droit),
                self.hauteur(arbre.gauche)
                )

        return return_val

    def afficher(self, arbre=None) -> str:
        if arbre is None:
            arbre = self
        if arbre.gauche is None and arbre.droit is None:
            return_val = str(arbre.valeur)

        elif arbre.gauche is None and arbre.droit is not None:
            return_val = str(arbre.valeur) + " " + self.afficher(arbre.droit)

        elif arbre.droit is None and arbre.gauche is not None:
            return_val = str(arbre.valeur) + " " + self.afficher(arbre.gauche)

        else:
            return_val = str(arbre.valeur) + " " + \
                self.afficher(arbre.gauche) + " " + self.afficher(arbre.droit)

        return return_val


if __name__ == "__main__":
    ex18 = ABR(32)
    val = [27, 35, 63, 18, 30, 28, 31, 8, 17]
    for i in val:
        ex18.inserer(i)
    print(" ".join(str(i) for i in [32] + val))
    print("______________________\n")
    print(ex18.afficher())
    print(ex18.taille())
    print(ex18.hauteur())
