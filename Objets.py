# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme


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


class Dinosaure:

    def __init__(self, longueur: int, hauteur: int, poids: int, vit_max: int) -> None:
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


if __name__ == "__name__":
    a = Chrono(12, 32, 21)
