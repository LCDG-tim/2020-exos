# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:42:57 2020

@author: Elève
"""

class Maillon:
    """class des maillons pour listes chainés
    """

    def __init__(self, valeur) -> None:
        self.val = valeur
        # None pour l'init
        self.suiv = None
        # None pour l'init
        self.prec = None

    def get_prec(self):
        return self.prec

    def get_val(self):
        return self.val

    def get_suiv(self):
        return self.suiv

    def set_suiv(self, new) -> None:
        self.suiv = new


class ListC:

    def __init__(self):
        self.tete = None

    def get_tete(self) -> None or Maillon:
        return self.tete

    def is_empty(self) -> bool:
        """O (1)"""
        return self.get_tete() is None

    def get_lengh(self) -> int:
        """O (n)"""
        n = 0
        if not self.is_empty():
            m = self.tete
            n = 1
            while m.suiv is not None:
                n += 1
                m = m.suiv
        return n

    def __len__(self) -> None:
        return self.get_lengh()

    def get_last_chaine(self) -> Maillon:
        """O (n)"""
        m = None
        if not self.is_empty():
            m = self.get_tete()
            while m.suiv is not None:
                m = m.suiv
        return m

    def get_maillon_indice(self, k: int) -> Maillon:
        """O (n/2)"""
        n_k = None
        if not self.is_empty():
            n_k = self.get_tete()
            for i in range(k):
                n_k = n_k.suiv
        return n_k

    def add_after(self, new_mail: Maillon, indix: int) -> None:
        """O (n)"""
        if not self.is_empty():
            new_mail.suiv = self.get_maillon_indice(indix)
            self.get_maillon_indice(indix - 1).suiv = new_mail

    def add_start(self, new: Maillon) -> None:
        """O (1)"""
        if not self.is_empty():
            new.suiv = self.tete
            self.tete = new

    def add_end(self, new: Maillon) -> None:
        """O (n)"""
        if not self.is_empty():
            self.get_last_chaine().suiv = new

    def delete_start(self) -> None:
        """O (1)"""
        if not self.is_empty():
            self.tete = self.tete.suiv

    def delete_end(self) -> None:
        """O (n)"""
        if not self.is_empty():
            self.get_maillon_indice(self.get_lengh() - 1).suiv = None

    def delete_after(self, indix: int) -> None:
        """O (n/2)"""
        if not self.is_empty():
            self.get_maillon_indice(indix).suiv = \
                self.get_maillon_indice(indix + 1).suiv

    def display(self) -> str:
        """O (n)"""
        return_val = ""
        if not self.is_empty():
            for i in range(self.get_lengh()):
                return_val += str(self.get_maillon_indice(i).val) + " "
        return return_val


if __name__ == "__main__":

    L: ListC = ListC()
    m_1: Maillon = Maillon(5)
    m_2: Maillon = Maillon(8)
    m_1.suiv = m_2
    m_3: Maillon = Maillon(3)
    m_1.suiv.suiv: Maillon = m_3
    L.tete = m_1
    print(
          L.is_empty(),
          L.get_lengh(),
          L.get_last_chaine().val,
          L.get_maillon_indice(0).val,
          L.get_maillon_indice(1).val,
          L.get_maillon_indice(2).val,
          sep="\n"
          )

    L.add_after(Maillon(4), 1)
    print(
        L.get_maillon_indice(0).val,
        L.get_maillon_indice(1).val,
        L.get_maillon_indice(2).val,
        L.display()
    )
