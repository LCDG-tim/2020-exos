 # -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:52:15 2020

@author: timot

algo Dijkstra
"""


class Matrice:

    def __init__(self, tabl):
        self.table = tabl

    def get_table(self):
        return self.table

    def get_max(self):
        pass

    def __str__(self):
        return ('\t{\n' +
                "\n".join((" ".join([str(j).center(4) for j in i]))
                          .center(len(self.table[0]) * 2 + len(self.table[0]))
        for i in self.table) + '\n}')


class Graph:

    def __init__(self, matrice):
        self.matrice = matrice

    def get_sommets(self) -> list:
        return [Sommet(str(i), j) for i in range(self.matrice) for j in self.matrice[i] if j != 0]

    def __str__(self):
        return str(self.matrice)

class Sommet:

    def __init__(self, nom: str, bind: list) -> None:
        self.bind = bind
        self.name = nom

    def distance(self, sommet) -> tuple:
        return self.distance


def algo_dijska(A: Graph, ligne: int, arrivee = 0) -> list:
    nb_pts = len(A.matrice.table)
    tabl = [None] * nb_pts
    vals = [None] * nb_pts
    tabl[ligne] = 0
    lignes_faites = list(range(nb_pts))
    lignes_faites.remove(ligne)
    run = True
    j = 0
    while run:
        print(j, tabl, vals)
        for i in lignes_faites:
            if A.matrice.table[j][i] != 0:
                vals.append(A.matrice.table[j][i])
                if tabl[i] is None:
                    tabl[i] = A.matrice.table[0][i]
                elif tabl[i] > A.matrice.table[j][i]:
                    tabl[i] = A.matrice.table[j][i]
        j = vals.index(min(vals))
        vals[j] = -1
        run = None in tabl
    return tabl





if __name__ == "__main__":
    a = (Graph(Matrice([
        [ 0,  18, 22,  0,  0,  0,  0,  0,  0,  0,  0],
        [18,   0, 31, 13, 26,  0,  0,  0,  0,  0,  0],
        [22,  31,  0,  0,  0, 17,  0,  0,  0,  0,  0],
        [ 0,  13,  0,  0,  0,  0, 24,  0,  0,  0,  0],
        [ 0,  26,  0,  0,  0, 12, 10,  0,  0,  0,  0],
        [ 0,   0, 17,  0, 12,  0,  0,  0, 13,  0,  0],
        [ 0,   0,  0, 24, 10,  0,  0, 13,  0,  0,  0],
        [ 0,   0,  0,  0,  0,  0, 13,  0,  7,  0, 25],
        [ 0,   0,  0,  0,  0, 13,  0,  7,  0, 13,  0],
        [ 0,   0,  0,  0,  0,  0,  0,  0, 13,  0, 18],
        [ 0,   0,  0,  0,  0,  0,  0, 25,  0, 18,  0]
        ]
        ))
    )
    print(a)
    print(algo_dijska(a, 0))
