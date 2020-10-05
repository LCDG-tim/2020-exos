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
            return_val = 0
        else:
            return_val = 1 + self.taille(arbre.gauche) \
                + self.taille(arbre.droit)
        return return_val

    def hauteur(self, arbre=None, i: int = 0) -> int:
        if arbre is None:
            arbre = self
        if arbre.droit is None and arbre.droit is None:
            return_val = i
        else:
            return_val = self.hauteur(arbre.gauche, i) + \
                self.hauteur(arbre.droite, i)
        return return_val

    def afficher(self, arbre=None, string: str = None) -> str:
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
    print(ex18.afficher())
    val = [27, 35, 63, 18, 30, 28, 31, 8, 17]
    for i in val:
        ex18.inserer(i)
    print(ex18.afficher())
