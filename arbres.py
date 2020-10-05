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


if __name__ == "__main__":
    ex18 = ABR(32)
    val = [27, 35, 63, 18, 30, 28, 31, 8, 17]
    for i in val:
        ex18.inserer(i)
