# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme


import math as m
import random as rdm


class Angle:

    def __init__(self, angle: int) -> None:
        self.angle = angle % 360

    def get_angle(self) -> int:
        return self.angle

    def afficher(self) -> str:
        return "{} degré".format(self.angle) + ("", "s")[self.angle > 1]

    def ajoute(self, angle) -> None:
        self.angle += angle.get_angle()
        if self.get_angle() > 360:
            self.angle %= 360

    def cosinus(self) -> float:
        return m.cos(m.radians(self.get_angle()))

    def sinus(self) -> float:
        return m.sin(m.radians(self.get_angle()))


class Date:

    def __init__(self, jour: int, mois: int, annee: int) -> None:
        self.day = jour
        self.month = mois
        self.year = annee
        self.__all_months = [
                "janvier",
                "février",
                "mars",
                "avril",
                "mai",
                "juin",
                "juillet",
                "août",
                "septembre",
                "octobre",
                "novembre",
                "décembre"
            ]

    def get_day(self) -> int:
        return self.day

    def get_month(self) -> int:
        return self.month

    def get_year(self) -> int:
        return self.year

    def __get_all_months(self, k: int = None) -> list:
        if k is not None:
            return_val = self.__all_months[k]
        else:
            return_val = self.__all_months
        return return_val

    def afficher(self) -> int:
        return "{} {} {}".format(
                self.get_day(),
                self.__get_all_months(self.get_month()),
                self.get_year()
            )

    def anterieur_a(self, date) -> bool:
        date: Date
        if self.get_year() >= date.get_year():
            return_val = False
        elif self.get_month() >= date.get_month():
            return_val = False
        elif self.get_day() >= date.get_day():
            return_val = False
        else:
            return_val = True
        return return_val


if __name__ == "__main__":
    print(Angle(180).sinus())
