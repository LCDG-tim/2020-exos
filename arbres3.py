 # -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:37:37 2020

@author: timot
"""


class ABR:
    def __init__(self,val):
        self.valeur=val
        self.gauche=None
        self.droite=None

    def inserer(self,x):

        if x<self.valeur:
            if self.gauche!=None:# si il y a un noeud à gauche
                self.gauche.inserer(x)
            else:
                self.gauche=ABR(x)
        else:
            if self.droite!=None:
                self.droite.inserer(x)
            else:
                self.droite=ABR(x)

    def affiche(self):
        """permet d'afficher un arbre"""
        if self == None: # si l'arbre est vide
            return None
        else :
            return [
                self.valeur,ABR.affiche(self.gauche),ABR.affiche(self.droite)
                ]

    def taille(self):
        """donne la taille d'un arbre cad le nombre de feuilles """
        if self==None:
            return 0
        else :
            return 1+ABR.taille(self.gauche)+ABR.taille(self.droite)

    def rechecher(self, val) -> bool:
        ret_val = False
        if self.valeur > val:
            if self.gauche is not None:
                ret_val = self.gauche.rechecher(val)
        elif self.valeur < val:
            if self.droite is not None:
                ret_val = self.droite.rechecher(val)
        else:
            ret_val = True
        return ret_val

    def hauteur(self):
        if self==None:
            return 0
        elif self.gauche==None and self.droite==None:
            return 0
        else :
            return 1+max(ABR.hauteur(self.gauche),ABR.hauteur(self.droite))

        def getValeur(self):
            return self.valeur

    def mini(self):
        if self.gauche is None:
            return self.valeur
        else:
            return self.gauche.mini()

    def maxi(self):
        if self.droite is None:
            return self.valeur
        else:
            return self.droite.maxi()


def listeEnArbre(l: list):
    abr = ABR(l[0])
    for i in l[1:]:
        abr.inserer(i)
    return abr


if __name__ == "__main__":
    a = listeEnArbre([45,245,185,15,6,165,15,456,465,46,451,56,16,446])