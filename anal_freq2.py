 # -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:57:56 2020

@author: timot
"""

def f(x: int):
    return ((3 * x + 7) % 26) + 65

table = {chr(i): chr(f(i)) for i in range(65, 91)}


def get_txt():
    with open("vh2.txt") as f:
        txt = f.read().rstrip("\n")
    txt = txt[3:]
    new = ""
    for i in txt:
        new += table.get(i)
    return new

if __name__ == "__main__":
    print(get_txt())
