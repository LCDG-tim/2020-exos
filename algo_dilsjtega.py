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

    def __str__(self):
        return '\t{\n' + "\n".join(str(" ".join([str(j) for j in i]))
        for i in self.table) + '\n}'


class Graph:

    def __init__(self, matrice):
        self.matrice = matrice

    def __str__(self):
        return str(self.matrice)


def algo_dijska(A: Graph):
    pass



if __name__ == "__main__":
    print(Graph(Matrice([
        [23, 33, 45],
        [23, 43, 61],
        [45, 54, 45]
        ]
        ))
    )
