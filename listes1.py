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


class ListC:
    
    def __init__(self):
        self.tete = None
        
    def get_tete(self) -> None or Maillon:
        return self.tete
        
    def is_empty(self) -> bool:
        return self.get_tete() is None
    
    def lengh(self) -> int:
        n = 0
        if not self.is_empty():
            m = self.tete
            n = 1
            while m.suiv is not None:
                n += 1
                m = m.suiv
        return n
    
    def get_last_chaine(self) -> Maillon:
        m = None
        if not self.is_empty():
            m = self.get_tete()
            while m.suiv is not None:
                m = m.suiv
        return m
    
    def get_maillon_indice(self, k: int):
        n_k = None
        if not self.is_empty():
            n_k = self.get_tete()
            for i in range(k):
                n_k = n_k.suiv
        return n_k
    
    def insert_new_m(self, new_mail: Maillon, indix: int) -> None:
        new_mail.suiv = self.get_maillon_indice(indix)
        self.get_maillon_indice(indix - 1).suiv = new_mail


L: ListC = ListC()
m_1: Maillon = Maillon(5)
m_2: Maillon = Maillon(8)
m_1.suiv = m_2
m_3: Maillon = Maillon(3)
m_1.suiv.suiv: Maillon = m_3
L.tete = m_1
print(
      L.is_empty(),
      L.lengh(),
      L.get_last_chaine().val,
      L.get_maillon_indice(0).val,
      L.get_maillon_indice(1).val,
      L.get_maillon_indice(2).val,
      sep="\n"
      )

L.insert_new_m(Maillon(4), 1)
print(
    L.get_maillon_indice(0).val,
    L.get_maillon_indice(1).val,
    L.get_maillon_indice(2).val,
)