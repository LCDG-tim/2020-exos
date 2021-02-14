 # -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 09:43:27 2020

@author: timot
"""


from timeit import default_timer as timer


# ex 1 1.
def occurence(mot: str, phrase: str, indice: int) -> bool:
    return phrase[indice:indice + len(mot)] == mot


def ex1b():
    # ex 1 3.
    i = 0
    lmot = len(mot)
    lphrase = len(phrase)
    a = i <= lphrase - lmot
    while not occurence(mot1, phrase, i) and a:
        i += 1
        a = i <= len(phrase) - len(mot)
    print(i)


# ex 2
def recherche(mot: str, phrase: str) -> int or str:
    i = 0
    lmot = len(mot)
    lphrase = len(phrase)
    a = i <= lphrase - lmot
    while not occurence(mot1, phrase, i) and a:
        i += 1
        a = i <= lphrase - lmot
    if not a:
        return("occurence non trouve")
    else:
        return(i)


# ex 3
def recherche2(mot: str, phrase: str) -> int or str:
    return [i
            for i in range(len(phrase) - len(mot))
            if occurence(mot, phrase, i)]


# ex 4
def ex4():
    with open('vh.txt','r') as vh:
        tome1 = vh.read()
    d=timer()
    for i in range(5):
        recherche2('a', tome1)
    f=timer()
    return(f - d)


def dico(mot):
    dico = {}
    m = len(mot) - 1
    for i in range(m):
        dico[mot[i]] = m - i
    return dico

def boyer_moore(mot: str, text: str) -> list:
    lmot, ltext  = len(mot), len(text)
    positions = []
    decalage = dico(mot)
    i = 0
    j = lmot - 1
    trouver = True
    while i <=  ltext - lmot and trouver:
        if text[i + j] != mot[j]:
            a = decalage[text[i + j]]
            if a is not None:
                if a < j:
                    i += a + j
            else:
                i += j + 1
            trouver = False
        else:
            trouver = True
        if trouver:
            positions.append(i)
            i += 1
        j -= 1
    return positions


if __name__ == "__main__":
    phrase = "Ceci n'est que la phrase qui nous sert d'exemple"
    mot1 = "qui"
    mot2 = "quiche"
    phrase2="CAAGCGCACAAGACGCGGCAGACCTTCGTTATAGGCGATGATTTCGAACCTACTAGTGGGT" \
        "CTCTTAGGCCGAGCGGTTCCGAGAGATAGTGAAAGATGGCTGGGCTGTGAAGGGAAGGAGTCGT" \
        "GAAAGCGCGAACACGAGTGTGCGCAAGCGCAGCGCCTTAGTATGCTCCAGTGTAGAAGCTCCGG" \
        "CGTCCCGTCTAACCGTACGCTGTCCCCGGTACATGGAGCTAATAGGCTTTACTGCCCAATATGA" \
        "CCCCGCGCCGCGACAAAACAATAACAGTTTGCTGTATGTTCCATGGTGGCCAATCCGTCTCTTT" \
        "TCGACAGCACGGCCAATTCTCCTAGGAAGCCAGCTCAATTTCAACGAAGTCGGCTGTTGAACAG" \
        "CGAGGTATGGCGTCGGTGGCTCTATTAGTGGTGAGCGAATTGAAATTCGGTGGCCTTACTTGTA" \
        "CCACAGCGATCCCTTCCCACCATTCTTATGCGTCGTCTGTTACCTGGCTTGGCAT"
    mot = "ACG"

    # ex 1 2.
    print(occurence(mot1, phrase, 2))
    print(recherche2(mot, phrase2))
    print(dico("comment"))
    print(boyer_moore(mot, phrase2))