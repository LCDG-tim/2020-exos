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

        r_is_none = arbre.droit is None
        l_is_none = arbre.gauche is None

        if r_is_none and l_is_none:
            return_val = 1

        elif r_is_none and not l_is_none:
            return_val = 1 + self.taille(arbre.gauche)

        elif not r_is_none and l_is_none:
            return_val = 1 + self.taille(arbre.droit)

        else:
            return_val = 1 + self.taille(arbre.gauche) \
                + self.taille(arbre.droit)

        return return_val

    def lengh(self) -> int:
        arbre_gauche = self.gauche.lengh() if self.gauche else 0
        arbre_droite = self.droit.lengh() if self.droit else 0

        return 1 + arbre_gauche + arbre_droite

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

    def hight(self) -> int:
        arbre_gauche = self.gauche.hight() if self.gauche else 0
        arbre_droit = self.droit.hight() if self.droit else 0
        return 1 + max(arbre_gauche, arbre_droit)

    def afficher(self, arbre=None) -> str:

        if arbre is None:
            arbre = self

        r_is_none = arbre.droit is None
        l_is_none = arbre.gauche is None

        if r_is_none and l_is_none:
            return_val = str(arbre.valeur)

        elif l_is_none and not r_is_none:
            return_val = str(arbre.valeur) + " " + self.afficher(arbre.droit)

        elif r_is_none and not l_is_none:
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
    print(ex18.lengh())
    print(ex18.hauteur())
    print(ex18.hight())
