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
        for i in self.table) + '\n}\n')


class Graph:

    def __init__(self, matrice):
        self.matrice = matrice

    def __str__(self):
        return str(self.matrice)



def bind(n : int) -> str:
    return chr(65 + n)

def debind(n: str) -> int:
    return ord(n) - 65


def algo_dijska(A: Graph, ligne: int, arrivee = "K") -> tuple:
    ligne = debind(ligne)
    nb_pts = len(A.matrice.table)
    tabl = [None] * nb_pts
    tabl[ligne] = (0, 0)
    distance = 0
    colonne_lock = [None] * nb_pts

    j = ligne
    colonne_lock[j] = j
    while colonne_lock != list(range(nb_pts)):
        for i in range(nb_pts):
            # print(i, j, A.matrice.table[j][i], tabl)
            if A.matrice.table[j][i] != 0:

                new_distance = distance + A.matrice.table[j][i]
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
        a[bind(i)] = (tabl[i][0], bind(tabl[i][1]))

    def get_chemin(a: dict, last = arrivee) -> str:
        if last == bind(ligne):
            return last
        else:
            return get_chemin(a, a[last][1]) + "-" + last

    chemin = get_chemin(a)

    return a[arrivee][0], chemin




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
    print("\n", algo_dijska(a, "A", "K"), sep="\n")
    print("\n", algo_dijska(a, "A"), sep="\n")
