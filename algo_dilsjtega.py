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
    tabl[ligne] = (0, 0)
    distance = 0
    colonne_lock = []

    j = ligne
    colonne_lock.append(j)
    for i in range(nb_pts):
        # print(i, j, A.matrice.table[j][i], tabl)
        distance = tabl[j][0]
        if A.matrice.table[j][i] != 0:

            new_distance = distance + A.matrice.table[j][i]
            if tabl[i] is None:
                tabl[i] = (A.matrice.table[0][i], j)

            elif tabl[i][0] > new_distance:
                tabl[i] = (new_distance, j)

    tabl_min = [tabl[i]
                for i in range(len(tabl))
                if i not in colonne_lock if i is not None]
    print("\n" + str(tabl_min) + "\n", colonne_lock)

    min_distance = tabl_min[0]

    for i in tabl_min:
        i: tuple
        if i is not None:

            if i[0] < min_distance[0]:
                min_distance = i
    print(min_distance)
    j = tabl.index(min_distance)
    colonne_lock.append(j)
    distance = min_distance[0]

    for i in range(nb_pts):
        # print(i, j, A.matrice.table[j][i], tabl)
        if A.matrice.table[j][i] != 0:

            new_distance = distance + A.matrice.table[j][i]
            if tabl[i] is None:
                tabl[i] = (new_distance, j)

            elif tabl[i][0] > new_distance:
                tabl[i] = (new_distance, j)

    tabl_min = [tabl[i]
                for i in range(len(tabl))
                if i not in colonne_lock]
    print("\n" + str(tabl_min) + "\n", colonne_lock)

    min_distance = tabl_min[0]
    for i in tabl_min:
        i: tuple
        if i is not None:

            if i[0] < min_distance[0]:
                min_distance = i
    print(min_distance)
    j = tabl.index(min_distance)
    colonne_lock.append(j)
    distance = min_distance[0]

    for i in range(nb_pts):
        # print(i, j, A.matrice.table[j][i], tabl)
        if A.matrice.table[j][i] != 0:

            new_distance = distance + A.matrice.table[j][i]
            if tabl[i] is None:
                tabl[i] = (new_distance, j)

            elif tabl[i][0] > new_distance:
                tabl[i] = (new_distance, j)

    tabl_min = [tabl[i]
                for i in range(len(tabl))
                if i not in colonne_lock]
    print("\n" + str(tabl_min) + "\n", colonne_lock)

    min_distance = tabl_min[0]
    for i in tabl_min:
        i: tuple
        if i is not None:

            if i[0] < min_distance[0]:
                min_distance = i
    print(min_distance)
    j = tabl.index(min_distance)
    colonne_lock.append(j)
    distance = min_distance[0]

    for i in range(nb_pts):
        # print(i, j, A.matrice.table[j][i], tabl)
        if A.matrice.table[j][i] != 0:

            new_distance = distance + A.matrice.table[j][i]
            if tabl[i] is None:
                tabl[i] = (new_distance, j)

            elif tabl[i][0] > new_distance:
                tabl[i] = (new_distance, j)

    tabl_min = [tabl[i]
                for i in range(len(tabl))
                if i not in colonne_lock]
    print("\n" + str(tabl_min) + "\n", colonne_lock)


    min_distance = tabl_min[0]
    for i in tabl_min:
        i: tuple
        if i is not None:

            if i[0] < min_distance[0]:
                min_distance = i
    print(min_distance)
    j = tabl.index(min_distance)
    colonne_lock.append(j)
    distance = min_distance[0]

    for i in range(nb_pts):
        # print(i, j, A.matrice.table[j][i], tabl)
        if A.matrice.table[j][i] != 0:

            new_distance = distance + A.matrice.table[j][i]
            if tabl[i] is None:
                tabl[i] = (new_distance, j)

            elif tabl[i][0] > new_distance:
                tabl[i] = (new_distance, j)

    tabl_min = [tabl[i]
                for i in range(len(tabl))
                if i not in colonne_lock]
    print("\n" + str(tabl_min) + "\n", colonne_lock)


    tabl_min = [tabl[i]
                for i in range(len(tabl))
                if i not in colonne_lock]
    print("\n" + str(tabl_min) + "\n", colonne_lock)

    min_distance = tabl_min[0]
    for i in tabl_min:
        i: tuple
        if i is not None:

            if i[0] < min_distance[0]:
                min_distance = i
    print(min_distance)
    j = tabl.index(min_distance)
    colonne_lock.append(j)
    distance = min_distance[0]

    for i in range(nb_pts):
        # print(i, j, A.matrice.table[j][i], tabl)
        if A.matrice.table[j][i] != 0:

            new_distance = distance + A.matrice.table[j][i]
            if tabl[i] is None:
                tabl[i] = (new_distance, j)

            elif tabl[i][0] > new_distance:
                tabl[i] = (new_distance, j)

    tabl_min = [tabl[i]
                for i in range(len(tabl))
                if i not in colonne_lock]
    print("\n" + str(tabl_min) + "\n", colonne_lock)

    min_distance = tabl_min[0]
    for i in tabl_min:
        i: tuple
        if i is not None:

            if i[0] < min_distance[0]:
                min_distance = i
    print(min_distance)
    j = tabl.index(min_distance)
    colonne_lock.append(j)
    distance = min_distance[0]

    for i in range(nb_pts):
        # print(i, j, A.matrice.table[j][i], tabl)
        if A.matrice.table[j][i] != 0:

            new_distance = distance + A.matrice.table[j][i]
            if tabl[i] is None:
                tabl[i] = (new_distance, j)

            elif tabl[i][0] > new_distance:
                tabl[i] = (new_distance, j)

    tabl_min = [tabl[i]
                for i in range(len(tabl))
                if i not in colonne_lock]
    print("\n" + str(tabl_min) + "\n", colonne_lock)

    min_distance = tabl_min[0]
    for i in tabl_min:
        i: tuple
        if i is not None:

            if i[0] < min_distance[0]:
                min_distance = i
    print(min_distance)
    j = tabl.index(min_distance)
    colonne_lock.append(j)
    distance = min_distance[0]

    for i in range(nb_pts):
        # print(i, j, A.matrice.table[j][i], tabl)
        if A.matrice.table[j][i] != 0:

            new_distance = distance + A.matrice.table[j][i]
            if tabl[i] is None:
                tabl[i] = (new_distance, j)

            elif tabl[i][0] > new_distance:
                tabl[i] = (new_distance, j)

    tabl_min = [tabl[i]
                for i in range(len(tabl))
                if i not in colonne_lock]
    print("\n" + str(tabl_min) + "\n", colonne_lock)

    min_distance = tabl_min[0]
    for i in tabl_min:
        i: tuple
        if i is not None:

            if i[0] < min_distance[0]:
                min_distance = i
    print(min_distance)
    j = tabl.index(min_distance)
    colonne_lock.append(j)
    distance = min_distance[0]

    for i in range(nb_pts):
        # print(i, j, A.matrice.table[j][i], tabl)
        if A.matrice.table[j][i] != 0:

            new_distance = distance + A.matrice.table[j][i]
            if tabl[i] is None:
                tabl[i] = (new_distance, j)

            elif tabl[i][0] > new_distance:
                tabl[i] = (new_distance, j)

    tabl_min = [tabl[i]
                for i in range(len(tabl))
                if i not in colonne_lock]
    print("\n" + str(tabl_min) + "\n", colonne_lock)

    min_distance = tabl_min[0]
    for i in tabl_min:
        i: tuple
        if i is not None:

            if i[0] < min_distance[0]:
                min_distance = i
    print(min_distance)
    j = tabl.index(min_distance)
    colonne_lock.append(j)
    distance = min_distance[0]

    for i in range(nb_pts):
        # print(i, j, A.matrice.table[j][i], tabl)
        if A.matrice.table[j][i] != 0:

            new_distance = distance + A.matrice.table[j][i]
            if tabl[i] is None:
                tabl[i] = (new_distance, j)

            elif tabl[i][0] > new_distance:
                tabl[i] = (new_distance, j)

    tabl_min = [tabl[i]
                for i in range(len(tabl))
                if i not in colonne_lock]
    print("\n" + str(tabl_min) + "\n", colonne_lock)

    min_distance = tabl_min[0]
    for i in tabl_min:
        i: tuple
        if i is not None:

            if i[0] < min_distance[0]:
                min_distance = i
    print(min_distance)
    j = tabl.index(min_distance)
    colonne_lock.append(j)
    distance = min_distance[0]

    for i in range(nb_pts):
        # print(i, j, A.matrice.table[j][i], tabl)
        if A.matrice.table[j][i] != 0:

            new_distance = distance + A.matrice.table[j][i]
            if tabl[i] is None:
                tabl[i] = (new_distance, j)

            elif tabl[i][0] > new_distance:
                tabl[i] = (new_distance, j)

    print(colonne_lock)
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
    print("\n", algo_dijska(a, 0), sep="\n")
