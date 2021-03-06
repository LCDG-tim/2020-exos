# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 09:13:12 2020

@author: Elève
"""


from listes1 import Maillon, ListC


class ListPile(ListC):

    def __init__(self) -> None:
        super().__init__()

    def empiler(self, new: Maillon) -> None:
        self.add_end(new)

    def depiler(self) -> Maillon:
        if not self.is_empty():
            return_val = self.get_last_chaine().get_val()
            self.delete_end()
        return return_val

    def sommet(self) -> Maillon:
        print(self.tete)
        return self.get_tete().get_val()


class ListPile2:

    def __init__(self) -> None:
        self.lst = []

    def get_lst(self) -> list:
        self.lst

    def is_empty(self) -> None:
        return not bool(self.lst)

    def empiler(self, val) -> None:
        self.lst.append(val)

    def depiler(self):
        return_val = None
        if not self.is_empty():
            return_val = self.lst.pop()
        return return_val

    def sommet(self):
        return_val = None
        if not self.is_empty():
            return_val = self.lst[-1]
        return return_val

    def taille(self):
        return len(self.lst)


class ListFile(ListC):

    def __init__(self) -> None:
        super().__init__()

    def add(self, new: Maillon) -> None:
        if isinstance(new, Maillon):
            self.add_end(new)
        else:
            self.add_end(Maillon(new))


    def retire(self) -> Maillon:
        return_val = self.get_tete().get_val()
        self.delete_start()
        return return_val

    def __str__(self) -> str:
        string = "["
        if not self.is_empty():
            m = self.tete
            string += "{}, ".format(m.get_val())
            while m.suiv is not None:
                string += "{}, ".format(m.get_val())
                m = m.suiv
        string += "]"
        return string

    def premier(self) -> Maillon:
        return self.get_last_chaine().get_val()


class ListFile2:

    def __init__(self) -> None:
        self.lst = []

    def get_lst(self) -> list:
        return self.lst

    def is_empty(self) -> None:
        return not bool(self.lst)

    def ajout(self, val) -> None:
        self.lst.append(val)

    def retire(self):
        return_val = None
        if not self.is_empty():
            return_val = self.lst.pop(0)
        return return_val

    def premier(self):
        return_val = None
        if not self.is_empty():
            return_val = self.lst[0]
        return return_val

    def taille(self):
        return len(self.lst)


if __name__ == "__main__":
    pass
