 # -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:23:10 2020

@author: timot
"""


import turtle


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


def aller_retour(lengh: float,
                 angle: float) -> None:
    turtle.seth(angle)
    turtle.fd(lengh)
    turtle.bk(lengh)


def axe() -> None:
    turtle.speed(0)
    go_to(-340, 0)
    turtle.goto(340, 0)
    aller_retour(10, 150)
    aller_retour(10, -150)
    go_to(350, 10)
    turtle.write("D")
    go_to(0, 200)
    aller_retour(10, -60)
    aller_retour(10, 240)
    turtle.goto(0, -200)
    aller_retour(10, 60)
    aller_retour(10, 120)
    go_to(5, -20)
    turtle.write("O")
    turtle.speed(1)



def len_oa_prime(f_prime: float, len_ab: float, len_oa: float) -> float:
    return f_prime * len_oa / (f_prime + len_oa) if - len_oa != f_prime \
        else 0


def afficher_points() -> None:
    global f_prime, len_oa, len_ab
    f_prime = float(input("f' = OF' = "))
    turtle.speed(0)
    x_f_prime = f_prime

    go_to(x_f_prime, -5)
    aller_retour(10, 90)
    go_to(x_f_prime, - 20)
    turtle.write("F'")

    go_to(-x_f_prime, -5)
    aller_retour(10, 90)
    go_to(-x_f_prime, - 20)
    turtle.write("F")

    len_oa = -float(input("OA = -"))
    x_a = len_oa

    go_to(x_a, -5)
    aller_retour(10, 90)
    go_to(x_a, - 20)
    turtle.write("A")

    len_ab = float(input("AB = "))
    y_b = len_ab
    go_to(x_a - 5, y_b - 5)
    turtle.goto(x_a + 5, y_b + 5)
    go_to(x_a + 5, y_b - 5)
    turtle.goto(x_a - 5, y_b + 5)
    go_to(x_a + 10, y_b - 20)
    turtle.write("B")

    go_to()
    turtle.speed(1)


def afficher_image() -> None:
    oa_prime = len_oa_prime(f_prime, len_ab, len_oa)

    go_to(oa_prime, -5)
    aller_retour(10, 90)
    go_to(oa_prime - 2.5, 6)
    turtle.write("A'")

    a_primeb_prime = len_oa * len_ab  / oa_prime
    go_to(oa_prime - 5, a_primeb_prime - 5)
    turtle.goto(oa_prime + 5, a_primeb_prime + 5)
    go_to(oa_prime + 5, a_primeb_prime - 5)
    turtle.goto(oa_prime - 5, a_primeb_prime + 5)
    go_to(oa_prime, a_primeb_prime - 20)
    turtle.write("B'")


if __name__ == "__main__":
    turtle.clear()
    axe()
    afficher_points()
    afficher_image()

    turtle.done()
