 # -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:07:49 2020

@author: timot
"""

import math


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-2) + fibo(n-1)


def fib_mem(n):
    mem = [0] * (n+1) #permet de créer un tableau contenant n+1 zéro
    return fib_rec(n, mem)


def fib_rec(n, mem):
    if n == 0 or n == 1:
        mem[n] = n
        return n
    elif mem[n] > 0:
        return mem[n]
    else:
        mem[n] = fib_rec(n-1, mem) + fib_rec(n-2, mem)
        return mem[n]


def glouton(n):
    pieces = [100, 50, 10, 5, 2, 1]
    nb_de_piece = []
    i = 0
    while n > 0:
        nb = n // pieces[i]
        if nb > 0:
            n -= pieces[i] * nb
            nb_de_piece += [pieces[i]] * nb
        i += 1
    return nb_de_piece


def rendu_monnaie_mem(P,X):
    mem = [0]*(X+1)
    return rendu_monnaie_mem_c(P,X,mem)


def rendu_monnaie_mem_c(P,X,m):
    if X==0:
        return 0
    elif m[X]>0:
        return m[X]
    else:
        mini = 1000
        for i in range(len(P)):
            if P[i]<=X:
                nb=1+rendu_monnaie_mem_c(P,X-P[i],m)
                if nb<mini:
                    mini = nb
                    m[X] = mini
    return mini

pieces = (2,5,10,50,100)
if __name__ == "__main__":
    print(fact(5))
