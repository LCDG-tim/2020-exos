# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:49:29 2020

@author: Elève
"""


class Dico:

    def __init__(self) -> None:
        self.lst = []
        self.cles = []

    def get_lst(self) -> list:
        return self.lst

    def get_cles(self) -> list:
        return self.cles

    def is_empty(self) -> bool:
        return bool(self.get_lst())

    def get_taille(self) -> int:
        return len(self.get_lst())

    def ajout(self, cle, val) -> None:
        self.get_lst().append(val)
        self.get_cles().append(cle)

    def modif(self, cle, val) -> None:
        if not self.is_empty():
            i = 0
            while self.get_cles()[i] != cle and i < self.get_taille():
                i += 1
            self.lst[i] = val

    def cle_indix(self, cle) -> bool:
        i = 0
        while cle != self.get_cles()[i] and i < len(self.get_cles()):
            i += 1
        if cle != self.get_cles()[i] and i == len(self.get_cles()):
            i = None
        return i

    def suppr(self, cle) -> None:
        if not self.is_empty():
            self.lst.pop(self.cle_indix(cle))

    def rech(self, cle):
        return_val = None
        if not self.is_empty():
            return_val = self.get_lst()[self.cle_indix(cle)]
        return return_val



if __name__ == "__main__":
    pass
