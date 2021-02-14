# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:52:15 2020.

@author: timot

algo Dijkstra
"""


# import random


# import networkx as nx
# import matplotlib.pyplot as plt


from list_pile import ListPile, ListFile2


class Matrice:
    """A representation of a matrix can do calculs with.

    builder and others method
    """

    def __init__(self, tabl: list):
        """
        Another description.

        Parameters
        ----------
        tabl : list
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.table = tabl

    def get_table(self):
        """
        Get the list of list of adjacence.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.table

    def get_max(self):
        """
        Get the maxi.

        Returns
        -------
        maxi : TYPE
            DESCRIPTION.

        """
        maxi = 0
        for i in self.table:
            if maxi < max(i):
                maxi = max(i)
        return maxi

    def __str__(self):
        """
        Give a str represention of a adjcence matrix.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return ('\t{\n' +
                "\n".join((" ".join([str(j).center(4) for j in i]))
                          .center(len(self.table[0]) * 2 + len(self.table[0]))
                          for i in self.table) + '\n}\n')

    def __list__(self) -> list:
        """
        Return the table of the matrix.

        Returns
        -------
        list
            DESCRIPTION.

        """
        return self.table

    def __len__(self) -> int:
        """
        Return the nomber of nods.

        Returns
        -------
        int
            DESCRIPTION.

        """
        return len(self.table)


class Graph:
    """A representation of a graph.

    its all
    """

    def __init__(self,
                 dic: dict = None,
                 matrice: Matrice = None,
                 titre: str = "defalut") -> None:
        """
        Another description.

        Parameters
        ----------
        dic : dict, optional
            DESCRIPTION. The default is None.
        matrice : Matrice, optional
            DESCRIPTION. The default is None.
        titre : str, optional
            DESCRIPTION. The default is "defalut".

        Returns
        -------
        None
            DESCRIPTION.

        """
        self.title = titre
        if dic is None and matrice is None:
            self.matrice = Matrice([[0, 0], [0, 0]])

        if dic is None:
            self.matrice = matrice
            self.dict = self.get_dict_by_matrice(self.matrice)

        elif matrice is None:
            self.dict = dic
            self.matrice = self.get_matrice_by_dict(dic)

    def get_dict_by_matrice(self, mat: dict) -> dict:
        """
        Another description.

        Parameters
        ----------
        mat : dict
            DESCRIPTION.

        Returns
        -------
        dict
            DESCRIPTION.

        """
        return {chr(65 + k): [chr(65 + j)
                    for j, l in enumerate(i)
                    if l > 0]
                for k, i in enumerate(self.matrice.table)
                }

    def get_matrice_by_dict(self, dic: dict) -> Matrice:
        """
        Another description.

        Parameters
        ----------
        dic : dict
            DESCRIPTION.

        Returns
        -------
        Matrice
            DESCRIPTION.

        """
        return Matrice([[1 for j in i] for i, k in self.dict.items()])

    def get_nb_sommets(self) -> int:
        """
        Another description.

        Returns
        -------
        int
            DESCRIPTION.

        """
        return len(self.dict)

    def nb_arretes(self) -> int:
        """
        Another description.

        Returns
        -------
        int
            DESCRIPTION.

        """
        nb = 0
        for i, j in self.dict.items():
            nb += len(j)
        return nb // 2

    def get_sommet_degres(self, sommet: str) -> int:
        """
        Another description.

        Parameters
        ----------
        sommet : str
            DESCRIPTION.

        Returns
        -------
        int
            DESCRIPTION.

        """
        return len(self.dict.get(sommet.capitalize()))

    def max_degres(self) -> int:
        """
        Another description.

        Returns
        -------
        int
            DESCRIPTION.

        """
        maxi = 0
        for i, j in self.dict.items():
            if len(j) > maxi:
                maxi = len(j)
        return maxi

    def neightbours(self, sommet: str) -> int:
        """
        Another description.

        Parameters
        ----------
        sommet : str
            DESCRIPTION.

        Returns
        -------
        int
            DESCRIPTION.

        """
        return self.dict.get(sommet.capitalize())

    def get_nb_sommets_mat(self) -> int:
        """
        Another description.

        Returns
        -------
        int
            DESCRIPTION.

        """
        return len(self.matrice)

    def get_nb_arretes_mat(self) -> int:
        """
        Another description.

        Returns
        -------
        int
            DESCRIPTION.

        """
        nb = 0
        for i in self.matrice.table:
            for j in i:
                if j > 0:
                    nb += 1
        return nb // 2

    def get_sommet_degres_mat(self, sommet: str) -> int:
        """
        Another description.

        Parameters
        ----------
        sommet : str
            DESCRIPTION.

        Returns
        -------
        int
            DESCRIPTION.

        """
        degre = 0
        for i in self.matrice.table[ord(sommet.capitalize()) - 65]:
            if i > 0:
                degre += 1
        return degre

    def get_degre_max_mat(self) -> int:
        """
        Another description.

        Returns
        -------
        int
            DESCRIPTION.

        """
        maxi = 0
        for i in range(len(self.matrice)):
            if maxi < self.get_sommet_degres_mat(chr(i + 65)):
                maxi = self.get_sommet_degres_mat(chr(i + 65))
        return maxi

    def algo_dijska(self, depart: int = "A", arrivee: str = "B") -> tuple:
        """
        Another description.

        Parameters
        ----------
        depart : int, optional
            DESCRIPTION. The default is "A".
        arrivee : str, optional
            DESCRIPTION. The default is "B".

        Returns
        -------
        tuple
            DESCRIPTION.

        """
        if 97 <= ord(depart) <= 122:
            depart = chr(65 + ord(depart) - 97)
        depart = self.debind(depart)
        nb_pts = len(self.matrice.table)
        tabl = [None] * nb_pts
        tabl[depart] = (0, 0)
        distance = 0
        colonne_lock = [None] * nb_pts

        j = depart
        colonne_lock[j] = j
        while colonne_lock != list(range(nb_pts)):
            for i in range(nb_pts):
                # print(i, j, A.matrice.table[j][i], tabl)
                if self.matrice.table[j][i] != 0:

                    new_distance = distance + self.matrice.table[j][i]
                    if tabl[i] is None:
                        tabl[i] = (new_distance, j)

                    elif tabl[i][0] > new_distance:
                        tabl[i] = (new_distance, j)

            tabl_min = [tabl[i]
                        for i in range(nb_pts)
                        if i not in colonne_lock
                        if tabl[i] is not None]

            if tabl_min:
                min_distance = tabl_min[0]
                for i in tabl_min:
                    i: tuple
                    if i[0] < min_distance[0]:
                        min_distance = i
                j = tabl.index(min_distance)
                colonne_lock[j] = j
                distance = min_distance[0]

        a = {}
        for i in range(nb_pts):
            a[self.bind(i)] = (tabl[i][0], self.bind(tabl[i][1]))

        chemin = self.get_chemin(a, depart, arrivee)

        return a[arrivee][0], chemin

    def get_chemin(self, a: dict, depart: str, last: str) -> str:
        """
        Another description.

        Parameters
        ----------
        a : dict
            DESCRIPTION.
        depart : str
            DESCRIPTION.
        last : str
            DESCRIPTION.

        Returns
        -------
        str
            DESCRIPTION.

        """
        if last == self.bind(depart):
            return last
        else:
            return self.get_chemin(a, depart, a[last][1]) + "-" + last

    def __str__(self) -> str:
        """
        Another description.

        Returns
        -------
        str
            DESCRIPTION.

        """
        return str(self.matrice)

    def bind(self, n: int) -> str:
        """
        Another description.

        Parameters
        ----------
        n : int
            DESCRIPTION.

        Returns
        -------
        str
            DESCRIPTION.

        """
        return chr(65 + n)

    def debind(self, n: str) -> int:
        """
        Another description.

        Parameters
        ----------
        n : str
            DESCRIPTION.

        Returns
        -------
        int
            DESCRIPTION.

        """
        return ord(n) - 65

    def get_lowest_distance_AB(self, depart: str, arrivee: str) -> int:
        """
        Another description.

        Parameters
        ----------
        depart : str
            DESCRIPTION.
        arrivee : str
            DESCRIPTION.

        Returns
        -------
        int
            DESCRIPTION.

        """
        return self.algo_dijska(depart, arrivee)[0]

    def get_lowest_way_AB(self, depart: str, arrivee: str) -> str:
        """
        Another description.

        Parameters
        ----------
        depart : str
            DESCRIPTION.
        arrivee : str
            DESCRIPTION.

        Returns
        -------
        str
            DESCRIPTION.

        """
        return self.algo_dijska(depart, arrivee)

    def parcours_profondeur(self, sommet):
        """
        Another description.

        Parameters
        ----------
        sommet : TYPE
            DESCRIPTION.

        Returns
        -------
        sommets_fermes : TYPE
            DESCRIPTION.

        """
        sommet = sommet.capitalize()
        sommets_visites = []
        sommets_fermes = []
        p = ListPile()
        sommets_visites.append(sommet)
        p.empiler(sommet)
        while not p.is_empty():
            tmp = p.sommet()
            voisins = [y for y in self.voisin(tmp) if y not in sommets_visites]
            sorted(voisins)
            if voisins:
                v = voisins[0]
                sommets_visites.append(v)
                p.empiler(v)
            else:
                sommets_fermes.append(tmp)
                p.depiler()
        return sommets_fermes

    def voisin(self, sommet: str) -> list:
        """
        Another description.

        Parameters
        ----------
        sommet : TYPE
            DESCRIPTION.

        Returns
        -------
        list
            DESCRIPTION.

        """
        return self.dict[sommet.capitalize()]

    def parcours_largeur(self, dep: str) -> None:
        """
        Parcours en largeur.

        Parameters
        ----------
        dep : str
            DESCRIPTION.

        Returns
        -------
        None
            DESCRIPTION.

        """
        return_val = []
        vois = self.voisin(dep)
        return_val.append(dep)
        for i in vois:
            return_val.append(i)
        for i in vois:
            for j in self.voisin(i):
                if j not in return_val:
                    return_val.append(i)
        return return_val

def voisin(G, sommet) -> list:
    """
    Another description.

    Parameters
    ----------
    G : TYPE
        DESCRIPTION.
    sommet : TYPE
        DESCRIPTION.

    Returns
    -------
    list
        DESCRIPTION.

    """
    return G[sommet]


def detection_cycle(G, sommet):
    """
    Detect the present of a cycle in a graph.

    Parameters
    ----------
    G : TYPE
        DESCRIPTION.
    sommet : TYPE
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.

    """
    sommets_visites = []
    f = ListFile2()
    sommets_visites.append(sommet)
    f.ajout((sommet, -1))
    while not f.is_empty():
        (tmp, parent) = f.retire()
        voisins = voisin(G, tmp)
    for vois in voisins:
        if vois not in sommets_visites:
            sommets_visites.append(vois)
            f.ajout((vois, tmp))
        elif vois != parent:
            return True
    return False



if __name__ == "__main__":
    a = (Graph(matrice=Matrice([
        [0,  18, 22,  0,  0,  0,  0,  0,  0,  0,  0],
        [18,  0, 31, 13, 26,  0,  0,  0,  0,  0,  0],
        [22, 31,  0,  0,  0, 17,  0,  0,  0,  0,  0],
        [0,  13,  0,  0,  0,  0, 24,  0,  0,  0,  0],
        [0,  26,  0,  0,  0, 12, 10,  0,  0,  0,  0],
        [0,   0, 17,  0, 12,  0,  0,  0, 13,  0,  0],
        [0,   0,  0, 24, 10,  0,  0, 13,  0,  0,  0],
        [0,   0,  0,  0,  0,  0, 13,  0,  7,  0, 25],
        [0,   0,  0,  0,  0, 13,  0,  7,  0, 13,  0],
        [0,   0,  0,  0,  0,  0,  0,  0, 13,  0, 18],
        [0,   0,  0,  0,  0,  0,  0, 25,  0, 18,  0]]),
        titre="evidence")
    )
    G = {}

    G['a'] = ['b', 'c']
    G['b'] = ['a', 'c', 'd', 'e']
    G['c'] = ['a', 'd', 'b']
    G['d'] = ['b', 'c', 'e']
    G['e'] = ['b', 'd', 'f', 'g']
    G['f'] = ['e', 'g']
    G['g'] = ['e', 'f', 'h']
    G['h'] = ['g']

    deplacement = [(i, j)
                   for i in range(-2, 3)
                   for j in range(-2, 3)
                   if i != 0 and j != 0]

    echec = {(i, j): [(i + k, j + l) for k, l in deplacement
                      if 0 < i + k < 8 and 0 < j + l < 8]
             for i in range(8)
             for j in range(8)}

    echiquier = Graph(titre="échiquier", dic=echec)

    # print("\n", a.algo_dijska("A", "K"), sep="\n")
    # print("\n", a.algo_dijska("B"), sep="\n")
