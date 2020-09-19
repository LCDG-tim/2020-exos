# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme


import math as m
import random as rdm


class Chrono:
    """class chrono pour temps
    """
    def __init__(
            self,
            annee: int,
            heures: int,
            minutes: int,
            secondes: int) -> None:
        """constructeur
        """
        self.annee = annee
        self.heures = heures
        self.minutes = minutes
        self.secondes = secondes

    def affiche(self) -> None:
        print("{}h {}m {}s".format(self.heures, self.minutes, self.secondes))

    def get_annee(self) -> int:
        return self.annee

    def get_heures(self) -> int:
        return self.heures

    def get_minutes(self) -> int:
        return self.minutes

    def get_secondes(self) -> int:
        return self.secondes

    def set_heures(self, new: int) -> None:
        self.heures = new


class Dinosaure:

    def __init__(
            self,
            longueur: int,
            hauteur: int,
            poids: int,
            vit_max: int) -> None:
        self.lengh = longueur
        self.hight = hauteur
        self.weight = poids
        self.max_speed = vit_max

    def get_lengh(self) -> int:
        return self.lengh

    def get_hight(self) -> int:
        return self.hight

    def get_weight(self) -> int:
        return self.weight

    def get_max_speed(self) -> int:
        return self.max_speed


class coord:

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        self.coord_tuple = (x, y)
        self.theta = self.calculer_theta(y / x)
        self.r = self.calculer_r(x, y)
        self.coord_pol_tuple = (self.r, self.theta)

    def get_x(self) -> float:
        return self.x

    def get_y(self) -> float:
        return self.y

    def get_r(self) -> float:
        return self.r

    def get_theta(self) -> float:
        return self.theta

    def get_coord_tuple(self) -> tuple:
        return self.coord_tuple

    def get_coord_polaire_tuple(self) -> tuple:
        return self.coord_pol_tuple

    def calculer_theta(self, x: float = None, y: float = None) -> float:
        def calcul(x: float, y: float) -> float:
            if x < 0:
                if y == 0:
                    return_val = m.pi
                elif y > 0:
                    return_val = m.atan(y / x) + m.pi
                else:
                    return_val = m.atan(y / x) - m.pi
            elif x == 0:
                if y > 0:
                    return_val = m.pi / 2
                elif y < 0:
                    return_val = -m.pi / 2
                else:
                    return_val = 0
            else:
                return_val = m.atan(x / y)
            return return_val

        if x is None and y is not None:
            return_val = calcul(y, self.x)
        elif x is not None and y is None:
            return_val = calcul(self.y, x)
        else:
            return_val = calcul(self.y, self.x)
        return return_val

    def calculer_r(self, x: float = None, y: float = None) -> float:
        if x is None and y is not None:
            return_val = m.sqrt(self.x ** 2 + y ** 2)
        elif x is not None and y is None:
            return_val = m.sqrt(x ** 2 + self.y ** 2)
        else:
            return_val = m.sqrt(self.x ** 2 + self.y ** 2)
        return return_val


class Domino:

    def __init__(self, g: int, d: int) -> None:
        self.left = g
        self.right = d

    def get_right(self) -> int:
        return self.right

    def get_left(self) -> int:
        return self.left

    def get_in_tuple(self) -> tuple:
        return self.get_left(), self.get_right()

    def afficher(self) -> None:
        if self.get_left() != self.get_right():
            print("""
 __ __
|{} | {}|
|__|__|
""".format(self.get_left(), self.get_right()))
        else:
            print("""
 __
|{} |
|__|
|{} |
|__|

""".format(self.get_left(), self.get_right()))

    def is_double(self, l: int = None, r: int = None) -> bool:
        if l is None and r is not None:
            return_val = self.left == r
        elif l is not None and r is None:
            new_l = l
            return_val = new_l == self.right
        else:
            return_val = self.left == self.right
        return return_val

    def is_white(self, l: int = None, r: int = None) -> bool:
        if l is None and r is not None:
            return_val = self.left == 0 and r == 0
        elif l is not None and r is None:
            new_l = l
            return_val = new_l == 0 and self.right == 0
        else:
            return_val = self.left == 0 and self.right == 0
        return return_val

    def nb_pts(self, l: int = None, r: int = None) -> int:
        if l is None and r is not None:
            return_val = self.left + r
        elif l is not None and r is None:
            return_val = l + self.right
        else:
            return_val = self.r + self.l
        return return_val


class Player:

    def __init__(self, jeu: list = []) -> None:
        self.jeu = jeu

    def get_jeu(self, k: int = None) -> list:
        if k is None:
            return_val = self.jeu
        else:
            return_val = self.jeu[k]
        return return_val

    def put_in_hand(self, new: Domino) -> None:
        self.jeu.append(new)

    def remove_of_hand(self, indix: int) -> None:
        self.jeu.remove()

    def afficher(self) -> None:
        print("jeu : {}".format(self.get_jeu()))


class JeuDeDomino:

    def __init__(self, nb_joueur: int) -> None:
        self.nb_players = nb_joueur
        self.dominos = [
                Domino(i, j)
                for i in range(7)
                for j in range(i + 1)
            ]
        self.pe_per_p = (7, 6)[nb_joueur >= 3]
        self.pioch = self.get_dominos().copy()
        self.jeu_per_players = [Player()] * self.get_nb_player()
        self.deal()
        self.shuffle()
        self.print_class()

    def get_nb_player(self) -> int:
        return self.nb_players

    def get_dominos(self, k: int = None) -> list:
        if k is None:
            return_val = self.dominos
        else:
            return_val = self.dominos[k]
        return return_val

    def get_pe_per_p(self) -> int:
        return self.pe_per_p

    def get_jeu_per_players(self, k: int = None) -> list:
        if k is None:
            return_val = self.jeu_per_players
        else:
            return_val = self.jeu_per_players[k]
        return return_val

    def get_pioche(self, k: int = None) -> list:
        if k is None:
            return_val = self.pioch
        else:
            return_val = self.pioch[k]
        return return_val

    def shuffle(self) -> None:
        rdm.shuffle(self.pioch)

    def deal(self) -> None:
        self.shuffle()
        for i in range(self.get_pe_per_p()):
            for j in self.get_jeu_per_players():
                j.put_in_hand(self.pioch.pop(0))

    def remove_pioche(self, k: int) -> None:
        del self.pioch[k]

    def print_class(self) -> None:
        print(
                "jeu de base : \n\t" +
                ", ".join([repr(i.get_in_tuple()) for i in self.get_dominos()])
            ),

        for i, j in enumerate(self.get_jeu_per_players(), start=1):
            j: Player
            print(
                    "jeu du joueur {}: \n\t".format(i) +
                    ", ".join([repr(k.get_in_tuple()) for k in j.get_jeu()])
                )
        print(
                "pioche : \n\t" +
                ", ".join(
                        repr(i.get_in_tuple())
                        for i in self.get_pioche()
                    )
            )


if __name__ == "__main__":
    a = Chrono(76, 12, 32, 21)
    trice = Dinosaure(9, 3, 9, 32)
    t_rex = Dinosaure(13, 6, 8, 27)
    A = coord(-2, 5)
    B = coord(5, 5)
    C = coord(-2, -2)
    D = coord(5, -2)
    e = JeuDeDomino(2)
