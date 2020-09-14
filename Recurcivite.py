# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme


import turtle


turtle.home()
turtle.clear()


def somme(n: int) -> int:
    """function who return the somme of all the number from 0 to n
    ----
    :pre:
        - n est un int
    :post:
        - somme est un int
    """

    assert isinstance(n, int), "n must be a int, not {}".format(type(n))
    assert n > 0, "n must be upper than 0, not {}".format(n)

    somme = 0
    for i in range(1, n + 1):
        somme += i

    assert isinstance(somme, int), \
        "somme must be a int, not {}".format(type(somme))
    return somme


def somme_recur(n: int) -> int:
    if n == 0:
        return_val = 0
    else:
        return_val = n + somme_recur(n - 1)
    return return_val


def fact_recur(n: int) -> int:
    """function factorial"""

    assert isinstance(n, int), "n must be a int, not {}".format(type(n))
    assert n > 0, "n must be upper than 0, not {}".format(n)

    if n == 1:
        return_val = 1
    else:
        return_val = n * fact_recur(n - 1)

    assert isinstance(return_val, int), "return_val must be a int, not {}"\
        .format(type(return_val))
    return return_val


def fact(n: int) -> int:
    """function fatorial"""
    assert isinstance(n, int), "n must be a int, not {}".format(type(n))
    assert n > 0, "n must be upper than 0, not {}".format(n)

    return_val = 1
    for i in range(1, n + 1):
        return_val *= i

    assert isinstance(return_val, int), "return_val must be a int, not {}"\
        .format(type(return_val))

    return return_val


def boucle_recur(i: int, k: int) -> None:
    if i == k:
        print(k)
    else:
        print(i)
        boucle_recur(i + 1, k)


def boucle(i: int, k: int) -> None:
    for j in range(i, k + 1):
        print(j)


def algo_multi(x: int, y: int) -> int:
    p = 0
    while x > 0:
        if x % 2 == 1:
            p += y
        x //= 2
        y += y
    return p


def algo_multi_recur(x: int, y: int) -> int:
    if x <= 0:
        return_val = 0
    elif x % 2 == 0:
        return_val = algo_multi_recur(x // 2, y * 2)
    else:
        return_val = algo_multi_recur(x // 2, y * 2) + y
    return return_val


def fibo(n: int) -> int:
    fn = 0
    fnplus1 = 1
    print("f0 = 0\nf1 = 1")
    for i in range(2, n + 1):
        a = fnplus1
        fnplus1 += fn
        fn = a
        print("f{} = {}".format(i, fnplus1))
    return fnplus1


def fibo_recur(n: int) -> int:
    if n < 2:
        return_val = n
    else:
        return_val = fibo_recur(n - 2) + fibo_recur(n - 1)
    return return_val


def von_koch(n: int, segment: int, col: str = None, y: int = None) -> None:
    colour = ("yellow", "blue", "red", "green", "purple")
    turtle.color(colour[n])
    if n > 0:
        for i in range(4):
            turtle.forward(segment // 3)
            turtle.left(60)
            if i == 1:
                turtle.left(180)
        von_koch(n // 3, segment // 3)
    return


def motif(n: int, seg: int) -> None:
    if n > 0:
        len_seg = seg // 3**n
        for i in range(4):
            turtle.forward(len_seg)
            turtle.left((60, 240)[i == 1])
        motif(n//2, seg)
    else:
        turtle.forward(seg)


def motiif(len_tri):
    turtle.forward(len_tri)
    turtle.left(60)
    turtle.forward(len_tri)
    turtle.left(-120)
    turtle.forward(len_tri)
    turtle.left(60)
    turtle.forward(len_tri)


def von_koch_itt(
        n: int,
        segment: int,
        color: str = "black",
        y: int = 0) -> None:

    # turtle init
    turtle.showturtle()
    turtle.penup()
    turtle.goto(0, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.speed(4)

    # color list
    colour = ("yellow", "blue", "red", "green", "purple")

    # lenght segments
    len_tri = segment // 3 ** n
    nb_mottif = 4 ** n
    a2n = True
    for i in range(nb_mottif):
        print(i, colour[i % len(colour)], i % 2 == 0 and a2n)
        turtle.color(colour[i % len(colour)])
        motiif(len_tri)
        nb = i % 2 == 0
        if nb:
            a2n = False
            turtle.left(60)
            a2n = True
        else:
            turtle.right(120)


def temoin(segm):
    turtle.penup()
    turtle.goto((0, -240))
    turtle.pendown()
    turtle.forward(segm)


if __name__ == "__main__":
    # print(somme(4))
    # print(somme_recur(4))
    # print(fact(4))
    # print(fact_recur(4))
    # boucle(0, 4)
    # boucle_recur(0, 4)
    # print(fibo(10))
    # print(fibo2(10))
    # print(algo_multi(105, 253))
    # print(algo_multi_recur(105, 253))
    # von_koch(0, 300)
    # motif(3, 100)
    # von_koch_itt(0, 100, "yellow", 0)
    i = 100
    temoin(i)
    von_koch(1, i, "red", -230)
    print("----------------------------------------------------------------")
    von_koch(2, i, "red", -200)
    print("----------------------------------------------------------------")
    von_koch(3, i, "red", 10)
    print("----------------------------------------------------------------")
    von_koch(3, i, "red", 30)
    pass
