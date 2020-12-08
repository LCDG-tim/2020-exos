 # -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:52:15 2020

@author: timot

algo Dijkstra
"""


import tkinter as tk


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

    def __init__(self, matrice: Matrice, titre: str) -> None:
        self.matrice = matrice
        self.title = titre

    def afficher(self) -> None:
        main = tk.Tk()
        main.geometry("500x500+100+100")
        main.title(self.title)
        main.minsize(500, 500)
        main.maxsize(main.winfo_screenwidth(), main.winfo_screenheight())
        main.config(bg="#888888")
        master_frame = tk.Frame(main, bg="#777777")

        points

        master_frame.pack(expand=tk.YES)
        main.mainloop()

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

    def bind(self, n : int) -> str:
        return chr(65 + n)

    def debind(self, n: str) -> int:
        return ord(n) - 65

    def get_lowest_distance_AB(self, depart: str, arrivee: str) -> int:
        return self.algo_dijska(depart, arrivee)[0]

    def get_lowest_way_AB(self, depart: str, arrivee: str) -> str:
        return self.algo_dijska(depart, arrivee)


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
        ), "evidence")
    )
    print(a)
    print("\n", a.algo_dijska("A", "K"), sep="\n")
    print("\n", a.algo_dijska("A"), sep="\n")
