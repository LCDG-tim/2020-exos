# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:52:15 2020

@author: timot

algo Dijkstra
"""


import random


import networkx as nx
import matplotlib.pyplot as plt


from list_pile import ListPile, ListFile, ListFile2


class Matrice:

    def __init__(self, tabl: list):
        self.table = tabl

    def get_table(self):
        return self.table

    def get_max(self):
        pass

    def __str__(self):
        return ('\t{\n' +
                "\n".join((" ".join([str(j).center(4) for j in i]))
                          .center(len(self.table[0]) * 2 + len(self.table[0]))
                          for i in self.table) + '\n}\n')

    def __list__(self) -> list:
        return self.table

    def __len__(self) -> int:
        return len(self.table)


class Graph:

    def __init__(self,
                 dic: dict = None,
                 matrice: Matrice = None,
                 titre: str = "defalut") -> None:
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
        return {chr(65 + k): [chr(65 + j)
                              for j, l in enumerate(i)
                              if l > 0]
                for k, i in enumerate(self.matrice.table)
                }

    def get_matrice_by_dict(self, dic: dict) -> Matrice:
        return Matrice([[1 for j in i] for i, k in self.dict.items()])

    def get_nb_sommets(self) -> int:
        return len(self.dict)

    def nb_arretes(self) -> int:
        nb = 0
        for i, j in self.dict.items():
            nb += len(j)
        return nb // 2

    def get_sommet_degres(self, sommet: str) -> int:
        return len(self.dict.get(sommet.capitalize()))

    def max_degres(self) -> int:
        maxi = 0
        for i, j in self.dict.items():
            if len(j) > maxi:
                maxi = len(j)
        return maxi

    def neightbours(self, sommet: str) -> int:
        return self.dict.get(sommet.capitalize())

    def get_nb_sommets_mat(self) -> int:
        return len(self.matrice)

    def get_nb_arretes_mat(self) -> int:
        nb = 0
        for i in self.matrice.table:
            for j in i:
                if j > 0:
                    nb += 1
        return nb // 2

    def get_sommet_degres_mat(self, sommet: str) -> int:
        degre = 0
        for i in self.matrice.table[ord(sommet.capitalize()) - 65]:
            if i > 0:
                degre += 1
        return degre

    def get_degre_max_mat(self) -> int:
        maxi = 0
        for i in range(len(self.matrice)):
            if maxi < self.get_sommet_degres_mat(chr(i + 65)):
                maxi = self.get_sommet_degres_mat(chr(i + 65))
        return maxi

    def algo_dijska(self, depart: int = "A", arrivee: str = "B") -> tuple:
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
        if last == self.bind(depart):
            return last
        else:
            return self.get_chemin(a, depart, a[last][1]) + "-" + last

    def __str__(self) -> str:
        return str(self.matrice)

    def bind(self, n: int) -> str:
        return chr(65 + n)

    def debind(self, n: str) -> int:
        return ord(n) - 65

    def get_lowest_distance_AB(self, depart: str, arrivee: str) -> int:
        return self.algo_dijska(depart, arrivee)[0]

    def get_lowest_way_AB(self, depart: str, arrivee: str) -> str:
        return self.algo_dijska(depart, arrivee)


def voisin(G, sommet):
    return G[sommet]


def parcours_profondeur(G, sommet):
    sommets_visites = []
    sommets_fermes = []
    p = ListPile()
    sommets_visites.append(sommet)
    p.empiler(sommet)
    while not p.vide():
        tmp = p.sommet()
        voisins = [y for y in voisin(G, tmp) if y not in sommets_visites]
        if voisins:
            v = random.choice(voisins)
            sommets_visites.append(v)
            p.empiler(v)
        else:
            sommets_fermes.append(tmp)
            p.depiler()
    return sommets_fermes


def detection_cycle(G, sommet):
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


def detect_cycle(graph: dict) -> bool:
    return


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

    print(detection_cycle(G, "a"))
    # print("\n", a.algo_dijska("A", "K"), sep="\n")
    # print("\n", a.algo_dijska("B"), sep="\n")
