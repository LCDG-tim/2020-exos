 # -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:34:03 2020

@author: timot
code tri fusion
"""

def fusion(L1: list, L2: list) -> list:
    i = 0
    j = 0
    k = len(L1)
    l = len(L2)
    m = []
    while i < k and j < l:
        if L1[i] < L2[j]:
            m.append(L1[i])
            i += 1
        else:
            m.append(L2[j])
            j += 1
    if i == k and j < l:
        m += L2[j:]
    elif i < k and j == l:
        m += L1[i:]
    return m


def tri_fusion(lst: list) -> list:
    if len(lst) == 1:
        return lst
    else:
        return fusion(
            tri_fusion(lst[:len(lst) // 2]),
            tri_fusion(lst[len(lst) // 2:]))


def mini(L1: list, L2: list) -> int:
    return [(L1[0], L2[0])[L2[0] < L1[0]]]


def get_mini(lst: list) -> int:
    if len(lst) == 1:
        return lst
    else:
        return mini(get_mini(lst[:len(lst) // 2]), get_mini(lst[len(lst) // 2:]))


def maxi(L1: list, L2: list) -> list:
    return [(L1[0], L2[0])[L2[0] > L1[0]]]


def get_maxi(lst: list) -> int:
    if len(lst) == 1:
        return lst
    else:
        return maxi(get_maxi(lst[:len(lst) // 2]), get_maxi(lst[len(lst) // 2:]))


if __name__ == "__main__":
    a = [3, 1661, 26, 614, 6, 16, 16, 100, 564, 21]
    print(a)
    print(get_mini(a))
    print(get_maxi(a))
    print(tri_fusion(a))
