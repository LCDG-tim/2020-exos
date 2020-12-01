 # -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:02:39 2020

@author: timot
"""


class ArbreBinaire:
    """Arbre binaire"""
    def __init__(self, val) -> None:
        """


        Parameters
        ----------
        val : TYPE
            DESCRIPTION.

        Returns
        -------
        None
            DESCRIPTION.

        """

        self.valeur = val
        self.gauche = None
        self.droite = None

    def inserer_gauche(self, valeur) -> None:
        """


        Parameters
        ----------
        valeur : TYPE
            DESCRIPTION.

        Returns
        -------
        None
            DESCRIPTION.

        """

        if self.gauche is None:
            self.gauche = ArbreBinaire(valeur)
        else:
            nouveau_noeud = ArbreBinaire(valeur)
            nouveau_noeud.gauche = self.gauche
            self.gauche = nouveau_noeud

    def inserer_droite(self, valeur) -> None:
        """


        Parameters
        ----------
        valeur : TYPE
            DESCRIPTION.

        Returns
        -------
        None
            DESCRIPTION.

        """

        if self.droite is None:
            self.droite = ArbreBinaire(valeur)
        else:
            nouveau_noeud = ArbreBinaire(valeur)
            nouveau_noeud.droite = self.droite
            self.droite = nouveau_noeud

    def affiche(self) -> list:
        """permet d'afficher un arbre avec None si le noeud n'a pas d'enfants
        """
        if self is None: # si l'arbre est vide
            return None
        else:
            return [
                self.valeur,
                ArbreBinaire.affiche(self.gauche),
                ArbreBinaire.affiche(self.droite)]

    def taille(self) -> int:
        """donne la taille d'un arbre cad le nombre de feuilles """
        if self is None:
            return 0
        else:
            return 1 + ArbreBinaire.taille(self.gauche) \
                + ArbreBinaire.taille(self.droite)

    def hauteur(self) -> int:
        """donne la haureur de l'arbre (la racine n'étant pas comptée)"""
        if self is None:
            return 0
        elif self.gauche is None and self.droite is None:
            return 0
        else:
            return 1 + max(ArbreBinaire.hauteur(self.gauche), \
                 ArbreBinaire.hauteur(self.droite))

    def get_valeur(self):
        """


        Returns
        -------
        TYPE
            DESCRIPTION.

        """

        return self.valeur

    def get_gauche(self):
        """


        Returns
        -------
        TYPE
            DESCRIPTION.

        """

        return self.gauche

    def get_droite(self):
        """


        Returns
        -------
        TYPE
            DESCRIPTION.

        """

        return self.droite


def parcours_infixe(abr: ArbreBinaire) -> None:
    """affiche les éléments de a dans un parcours infixe"""
    if abr is None:
        return None
    else:
        parcours_infixe(abr.gauche)
        print(abr.get_valeur(), end=' ')
        parcours_infixe(abr.droite)


def parcours_prefixe(abr: ArbreBinaire) -> None:
    """affiche tours les éléments de a dans un parcours préfixe"""
    if abr is None:
        return None
    else:
        print(abr.get_valeur(), end=' ')
        parcours_prefixe(abr.gauche)
        parcours_prefixe(abr.droite)



def parcours_suffixe(abr: ArbreBinaire) -> None:
    """affiche les éléments de a dans un parcours infixe"""
    if abr is None:
        return None
    else:
        parcours_suffixe(abr.gauche)
        parcours_suffixe(abr.droite)
        print(abr.get_valeur(), end=' ')


class Element:
    """Element liste chainee"""
    #chaque élément a pour attribut : le précédent , le suivant et
    # la valeur de l'élément
    def __init__(self, valeur):
        self.val = valeur
        self.precedent = None
        self.suivant = None

    def __str__(self): #methode qui permet de lance un print sur un tel objet
        return str(self.val) + "-" + str(self.suivant)


class File:
    """file : list FIFO"""
    # ici une file est la donnée de deux attributs : la file complète de type
    # Element et le dernier élément de la file de type Element
    def __init__(self) -> None:
        """


        Returns
        -------
        None
            DESCRIPTION.

        """

        self.tete = None
        self.queue = None

    def get_dernier_elt(self) -> Element:
        elt = None
        if not self.file_vide():
            elt = self.tete
            while elt.suivant is not None:
                elt = elt.suivant
        return elt

    def enfile(self, valeur) -> None:
        """


        Parameters
        ----------
        valeur : TYPE
            DESCRIPTION.

        Returns
        -------
        None
            DESCRIPTION.

        """

        elt = Element(valeur) #on transforme l'élément à ajouter en un objet Element
        # de listes doublement Chainées
        if self.tete is None:
            self.tete = elt #file vide la tete est remplacée par l'élément e
        else:
            elt.precedent = self.queue #le précédent de l'élément pointe sur
            # l'ancienne queue de la file
            self.queue.suivant = elt #l'ancienne queue de la file pointe sur
            # elt
            # avec suivant
            self.queue = elt # on redéfinit self.queue par e.
        self.queue = self.get_dernier_elt()

    def file_vide(self) -> bool:
        """


        Returns
        -------
        bool
            DESCRIPTION.

        """

        return self.tete is None #renvoie True si None et False sinon

    def defile(self):
        """


        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        if not self.file_vide():
            elt = self.tete #on stocke l'élément à defiler
        if elt.suivant is None: #cas où il n'y a qu'un élément
            self.tete = None
            self.queue = None
        else:
            self.tete = elt.suivant
            self.tete.precedent = None
        return elt.val

        def __str__(self):
            return str(self.tete)


def BFT(arbre):
    f=File()
    f.enfile(arbre)
    l=[]
    while not f.file_vide():
        a=f.defile()
        l.append(a.valeur)
        if a.gauche!=None:
            f.enfile(a.gauche)
        if a.droite!=None:
            f.enfile(a.droite)
    return l


if __name__ == "__main__":
    A = ArbreBinaire(8)
    A.inserer_gauche(9)
    A.inserer_droite(7)

    B = A.get_gauche()
    B.inserer_gauche(2)
    B.inserer_droite(11)

    C = B.get_droite()
    B.inserer_gauche(28)

    B = A.get_droite()
    B.inserer_droite(7)

    C = B.get_droite()
    C.inserer_droite(15)

    B = C.get_droite()
    B.inserer_droite(17)

    print(A.affiche())
    parcours_infixe(A)
    print("\n")
    parcours_prefixe(A)
    print("\n")
    parcours_suffixe(A)
    print("\n", BFT(A))
