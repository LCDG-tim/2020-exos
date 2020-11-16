 # -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 20:48:33 2020

@author: timot
"""


import random as rdm


import turtle
import math


base16 = ["1", "2", "3", "4", "5", "6", "7", "8", "9",
          "A", "B", "C", "D", "E", "F"]


def get_random_color() -> str:
    return "#" + "".join(rdm.choices(base16, k=6))


def go_to(x: int or float = 0, y: int or float = 0) -> None:
    """
    met la tortue là ou tu veut

    Parameters
    ----------
    x : int or float. The default is 0.
        Valeur de l'abcisse du point dans le plan orthonormé (O;i;j).
    y : int or float. The default is 0.
        Valeur de l'ordonnée du point dans le plan orthonormé (O;i;j).

    Returns
    -------
    None
        Procedure.

    """
    turtle.pu()
    turtle.goto((x, y))
    turtle.pd()


def get_x_turtle() -> int:
    return turtle.pos()[0]

def get_y_turtle() -> int:
    return turtle.pos()[1]


def start_a_filling(fill_color: str = "white",
                    border_color: str = "black") -> None:
    """


    Parameters
    ----------
    fill_color : str, optional
        DESCRIPTION. The default is "white".
    border_color : str, optional
        DESCRIPTION. The default is "black".

    Returns
    -------
    None
        DESCRIPTION.

    """

    turtle.color(border_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()


def polygone_regulier(nb_cotes:int = 4, lengh: int = 10,
                      fill_color: str = "white",
                      border_color: str = "black") -> None:
    """
    draw a regular polygone

    Parameters
    ----------
    nb_cotes : int, optional
        the number of sides. The default is 4.
    lengh : int, optional
        lengh of the square. The default is 10.
    fill_color : str, optional
        the inside color. The default is "white".
    border_color : str, optional
        the border color. The default is "black".

    Returns
    -------
    None
        Procedure.

    """
    start_a_filling(fill_color, border_color)
    for i in range(nb_cotes):
        turtle.fd(lengh)
        turtle.rt(360 / nb_cotes)
    turtle.end_fill()
    turtle.seth(0)


def rect(width: int = 40,
         height: int = 10,
         fill_color: str = "white",
         border_color: str = "black") -> None:
    """
    draw a rect

    Parameters
    ----------
    width : int, optional
        DESCRIPTION. The default is 40.
    height : int, optional
        DESCRIPTION. The default is 10.
    fill_color : str, optional
        DESCRIPTION. The default is "white".
    border_color : str, optional
        DESCRIPTION. The default is "black".

    Returns
    -------
    None
        DESCRIPTION.

    """

    start_a_filling(fill_color, border_color)
    for i in range(4):
        turtle.fd((width, height)[i % 2 == 1])
        turtle.lt(90)
    turtle.end_fill()
    turtle.seth(0)


class Element:

    def __init__(self, largeur: int = 30, hauteur: int = 30,
                 couleur_bordure: str = "black",
                 couleur_interieur: str = "white") -> None:
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur_bordure = couleur_bordure
        self.couleur_interieur = couleur_interieur

    def get_largeur(self) -> int:
        return self.largeur

    def get_hauteur(self) -> int:
        return self.hauteur

    def get_couleur_bordure(self) -> str:
        return self.couleur_bordure

    def get_couleur_interieur(self) -> str:
        return self.couleur_interieur



class Fenetre(Element):

    def __init__(self, pos: int, pos_etage: tuple) -> None:
        super().__init__()
        self.pos = pos
        self.posb = pos_etage
        self.pos2_x, self.pos2_y = pos_etage
        self.pos2_x += 15 + (self.pos - 1) * 40
        self.pos2_y += 50


    def afficher(self) -> None:
        if self.pos == 1:
            go_to(self.pos2_x, self.pos2_y)
        elif self.pos == 2:
            go_to(self.pos2_x, self.pos2_y)
        else:
            go_to(self.pos2_x, self.pos2_y)
        polygone_regulier(4, self.get_largeur())
        go_to(self.posb[0], self.posb[1])


class Balcon(Element):
    def __init__(self, pos: int, pos_etage: tuple) -> None:
        super().__init__(35, 40)
        self.pos = pos
        self.pos_etages = pos_etage

    def afficher(self) -> None:
        go_to()


class PorteFenetre(Element):

    def __init__(self, pos: int, pos_etage: tuple) -> None:
        super().__init__(30, 50)
        self.pos = pos
        self.posx, self.posy = pos_etage
        self.pos2_x, self.pos2_y = pos_etage
        self.pos2_x += 15 + (self.pos - 1) * 40

    def afficher(self) -> None:
        if self.pos == 1:
            go_to(self.pos2_x, self.pos2_y)
        elif self.pos == 2:
            go_to(self.pos2_x, self.pos2_y)
        else:
            go_to(self.pos2_x, self.pos2_y)
        rect(self.get_largeur(), self.get_hauteur())
        go_to(self.pos2_x, self.pos2_y)


class PorteEntre(Element):

    def __init__(self, pos: tuple, pos_p: int) -> None:
        super().__init__(30, 50, "black", get_random_color())
        self.pos = pos_p
        self.posxb, self.posy = pos
        self.posx = self.posxb + 15 + (self.pos - 1) * 40

    def afficher(self) -> None:
        if rdm.randint(0, 1):
            go_to(self.posx, self.posy)
            start_a_filling(self.couleur_interieur, self.couleur_bordure)
            turtle.goto(self.posx + self.largeur, self.posy)
            turtle.goto(self.posx + self.largeur, self.posy + self.hauteur
                        -20)
            turtle.seth(90)
            turtle.circle(self.largeur / 2, 180)
            turtle.goto(self.posx, self.posy + self.hauteur - 20)
            turtle.goto(self.posx, self.posy)
        else:
            go_to(self.posx, self.posy)
            rect(self.largeur, self.hauteur, self.get_couleur_interieur(),
                 self.get_couleur_bordure())
        turtle.end_fill()
        turtle.seth(0)
        go_to(self.posxb, self.posy)



class Etage(Element):

    def __init__(self, couleur: str) -> None:
        super().__init__(140, 60, "black", couleur)
        self.pos = (get_x_turtle(), get_y_turtle())
        print(self.pos)
        self.elts = [(Fenetre(i, self.pos), PorteFenetre(i, self.pos))[rdm.randint(0, 1)]
                     for i in range(1, 4)]

    def get_couleur(self) -> str:
        return self.couleur

    def get_longeur(self) -> int:
        return self.longeur

    def get_hauteur(self) -> int:
        return self.hauteur

    def get_window(self) -> int:
        return self.window

    def afficher(self) -> None:
        rect(self.largeur, self.hauteur, self.get_couleur_interieur())
        for i in self.elts:
            i.afficher()
        go_to(self.pos[0], self.pos[1] + self.hauteur)


class RezDeChaussee(Etage):

    def __init__(self, couleur: str) -> None:
        super().__init__(couleur)
        self.pos_porte = rdm.randint(1, 3)
        self.pos = (get_x_turtle(), get_y_turtle())
        self.pos_win = [1, 2, 3]
        self.pos_win.remove(self.pos_porte)
        print(self.pos_porte, self.pos_win)

    def afficher(self) -> None:
        rect(self.largeur, self.hauteur, self.get_couleur_interieur())
        PorteEntre(self.pos, self.pos_porte).afficher()
        for i in self.pos_win:
            Fenetre(i, self.pos).afficher()
        go_to(self.pos[0], self.pos[1] + self.hauteur)

class Immeubles(Element):

    def __init__(self, couleur: str, etages: int) -> None:
        super().__init__(140, (etages + 1) * 60, couleur_interieur=couleur)
        self.etages = etages

    def afficher(self) -> None:
        RezDeChaussee(self.get_couleur_interieur()).afficher()
        for i in range(self.etages):
            Etage(self.get_couleur_interieur()).afficher()


if __name__ == "__main__":
    immeuble1 = Immeubles(get_random_color(),
                          rdm.randint(0, 4))
    turtle.speed(0)
    immeuble1.afficher()
    go_to(-130, 0)
    turtle.goto(-130, 0)
    turtle.done()
