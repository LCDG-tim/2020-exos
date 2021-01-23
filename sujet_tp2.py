# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:48:06 2021

Fini en 9H

@author: loann
"""


from random import randint


# =============================================================================
# Sujet 1
# =============================================================================

def exo_S1(tab: list, n: int) -> int:
    tab.reverse()
    try:
        return(len(tab) - 1 - tab.index(n))
    except ValueError:
        return len(tab)


def distance(point1: tuple, point2: tuple):
    assert type(point1) == tuple, "le point1 n'est pas un tuple"
    assert type(point2) == tuple, "le point2 n'est pas un tuple"
    assert len(point1) == 2, "le point1 n'est pas composé de 2 éléments"
    assert len(point2) == 2, "le point2 n'est pas composé de 2 éléments"
    assert type(point1[0]) == int, "l'élément 1 du point1 n'est pas un entier"
    assert type(point1[1]) == int, "l'élément 2 du point1 n'est pas un entier"
    assert type(point2[0]) == int, "l'élément 1 du point2 n'est pas un entier"
    assert type(point2[1]) == int, "l'élément 2 du point2 n'est pas un entier"

    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** (1/2)


def plus_courte_distance(tab: list, depart: tuple):
    point = tab[0]
    min_dist = distance(point, depart)
    for i in range(1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point


# =============================================================================
# Sujet 2
# =============================================================================

def exo_S2(tab: list) -> float or str:
    if not len(tab):
        return 'erreur'
    else:
        return_val = 0
        for i in tab:
            return_val += i

        return return_val / len(tab)


def tri(tab: list):
    i = 0
    j = len(tab) - 1
    while i != j:
        if tab[i] == 0:
            i += 1
        else:
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j -= 1
    return tab


# =============================================================================
# Sujet 3
# =============================================================================

def exo_S3(n1: int, n2: int):
    return_val = 0

    for i in range(abs(n1)):
        return_val += n2

    if not(n1 >= 0 and n2 >= 0) or not(n1 < 0 and n2 < 0):
        return_val = -return_val

    return return_val


def dichotomie_S3(tab: list, x: int):
    debut = 0
    fin = len(tab) - 1

    while debut <= fin:
        m = (fin + debut) // 2
        if x == tab[m]:
            return True

        if x > tab[m]:
            debut = m + 1

        else:
            fin = m - 1

    return False


# =============================================================================
# Sujet 4
# =============================================================================

def exo_S4(tab: list) -> float:
    assert len(tab), 'Le tableau est vide'

    return_val = 0
    for i in tab:
        return_val += i

    return return_val / len(tab)


def dichotomie_S4(tab: list, x: int):

    if not len(tab):
        return False, 1

    if (x < tab[0]) or (x > tab[-1]):
        return False, 2

    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (fin + debut) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False, 3


# =============================================================================
# Sujet 5
# =============================================================================

def exo_S5(T: list) -> int:
    T.reverse()
    return_val = 0
    for i in range(len(T)):
        if T[i]:
            return_val += 2**i

    return return_val


def tri_insertion(L: list):
    n = len(L)

    if not n:
        return L

    for j in range(1, n):
        e = L[j]
        i = j

        while i > 0 and L[i-1] > e:
            i -= 1

        if i != j:
            for k in range(j, i, -1):
                L[k] = L[k-1]
            L[i] = e
    return L


# =============================================================================
# Sujet 6
# =============================================================================

def exo_S6(somme_a_rendre: int):
    monnaie = [5, 2, 1]
    return_val = [0 for i in monnaie]
    deja_rendu = 0
    for i in range(len(monnaie)):
        while deja_rendu + monnaie[i] <= somme_a_rendre:
            return_val[i] += 1
            deja_rendu += monnaie[i]

    return return_val


# Faute dans l'enoncer (class Maillon)
class Maillon:
    def __init__(self, v, suivant=None):
        self.valeur = v
        self.suivant = suivant


class File:
    def __init__(self):
        self.dernier_file = None

    def enfile(self, element):
        nouveau_maillon = Maillon(element, self.dernier_file)
        self.dernier_file = nouveau_maillon

    def est_vide(self):
        return not self.dernier_file

    def affiche(self):
        maillon = self.dernier_file
        while not maillon:
            print(maillon.valeur)
            maillon = maillon.suivant

    def defile(self):
        if not self.est_vide():
            if not self.dernier_file.suivant:
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = self.dernier_file
            while not maillon.suivant.suivant:
                maillon = maillon.suivant
            resultat = maillon.suivant.valeur
            maillon.suivant = None
            return resultat
        return None


# =============================================================================
# Sujet 7
# =============================================================================

def exo_S7_1(n: int):
    mem = [0] * (n + 1)
    return exo_S7_2(n, mem)


def exo_S7_2(n: int, mem: list):
    if n == 0 or n == 1:
        mem[n] = n
        return n

    elif mem[n] > 0:
        return mem[n]

    else:
        mem[n] = exo_S7_2(n-1, mem) + exo_S7_2(n-2, mem)
        return mem[n]


def meilleures_notes():
    liste_eleves = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    liste_notes = [1, 40, 80, 60, 58, 80, 75, 80, 60, 24]

    note_maxi = 0
    nb_eleves_note_maxi = 0
    liste_maxi = []

    for compteur in range(len(liste_eleves)):
        if liste_notes[compteur] == note_maxi:
            nb_eleves_note_maxi += 1
            liste_maxi.append(liste_eleves[compteur])
        if liste_notes[compteur] > note_maxi:
            note_maxi = liste_notes[compteur]
            nb_eleves_note_maxi = 1
            liste_maxi = [liste_eleves[compteur]]

    return (note_maxi, nb_eleves_note_maxi, liste_maxi)


# =============================================================================
# Sujet 8
# =============================================================================

def exo_S8(caractere: str, mot: str) -> int:
    return_val = 0
    for i in mot:
        if i == caractere:
            return_val += 1
    return return_val


# Faute dans l'enoncer (premier retrun)
def rendu_glouton(arendre: int, solution=[], i=0):
    pieces = [100, 50, 20, 10, 5, 2, 1]

    if arendre == 0:
        return solution
    p = pieces[i]

    if p <= arendre:
        solution.append(p)
        return rendu_glouton(arendre - p, solution, i)
    else:
        return rendu_glouton(arendre, solution, i + 1)


# =============================================================================
# Sujet 9
# =============================================================================

# Faute dans l'enoncer (resultat de l'exemple)
def exo_S9(resultat: list) -> float:
    return_val = 0
    total_coef = 0
    for i in resultat:
        return_val += i[0]*i[1]
        total_coef += i[1]

    return return_val / total_coef


def pascal(n: int):
    C = [[1]]
    for k in range(1, n+1):
        Ck = [1]
        for i in range(1, k):
            Ck.append(C[k-1][i-1]+C[k-1][i])
        Ck.append(1)
        C.append(Ck)
    return C


# =============================================================================
# Sujet 10
# =============================================================================


def exo_S10(tab: list) -> tuple:
    return max(tab), tab.index(max(tab))


def positif(T: list):
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = []
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ', T)
    return T2


# =============================================================================
# Sujet 11
# =============================================================================

# Faute dans l'enoncer (resultat exemple)
def exo_S11(n: int) -> tuple:
    b = []
    quotient = n
    while quotient > 0:
        b.append(quotient % 2)
        quotient //= 2
    b.reverse()
    return b, len(b)


def tri_bulle1(T: list):
    n = len(T)
    for i in range(n-1, -1, -1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T


def triBulle2(T: list):
    n = len(T)
    for i in range(n-1):
        for j in range(n - i - 1):
            if T[j] > T[j + 1]:
                T[j+1], T[j] = T[j], T[j+1]
    return T


# =============================================================================
# Sujet 12
# =============================================================================

def exo_S12(tab: list) -> tuple:
    return max(tab), tab.index(max(tab))


def recherche(gene: str, seq_adn: str):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n and not trouve:
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j += 1
        if j == g:
            trouve = True
        i += 1
    return trouve


# =============================================================================
# Sujet 13
# =============================================================================


def exo_S13(T: list):
    for i in range(len(T) - 1):
        index_min = T[i:].index(min(T[i:])) + i
        if T[i] != T[index_min]:
            T[index_min], T[i] = T[i], T[index_min]

    return T


def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1

    while nb_mystere != nb_test and compteur < 10:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print("Bravo ! Le nombre était ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre était ", nb_mystere)


# =============================================================================
# Sujet 14
# =============================================================================

def exo_S14(elt: int, tab: list) -> list:
    return_val = []
    while elt in tab:
        return_val.append(tab.index(elt) + len(return_val))
        tab.remove(elt)
    return return_val


def moyenne(nom: str):

    resultats = {'Dupont': {'DS1': [15.5, 4],
                            'DM1': [14.5, 1],
                            'DS2': [13, 4],
                            'PROJET1': [16, 3],
                            'DS3': [14, 4]},
                 'Durand': {'DS1': [6, 4],
                            'DM1': [14.5, 1],
                            'DS2': [8, 4],
                            'PROJET1': [9, 3],
                            'IE1': [7, 2],
                            'DS3': [8, 4],
                            'DS4': [15, 4]}}

    if nom in resultats.keys():
        notes = resultats[nom]
        total_points = 0
        total_coefficients = 0
        for valeurs in notes.values():
            note, coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round(total_points / total_coefficients, 1)
    else:
        return -1


# =============================================================================
# Sujet 15
# =============================================================================

def exo_S15(tab: list) -> dict:
    try:
        return {'min': min(tab), 'max': max(tab)}
    except ValueError:
        return {'min': None, 'max': None}


class Carte:
    def __init__(self, c: int, v: int):
        self.Couleur = c
        self.Valeur = v

    def getNom(self):
        if (self.Valeur > 1 and self.Valeur < 11):
            return str(self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle'][self.Couleur]


class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    def remplir(self):
        for i in range(1, 14):
            for j in range(1, 5):
                self.contenu.append(Carte(j, i))

    def getCarteAt(self, pos):
        return self.contenu[pos]


# =============================================================================
# Sujet 16
# =============================================================================

def exo_S16(tab: list):
    return_val = 0
    for i in tab:
        return_val += i

    return return_val / len(tab)


def dec_to_bin(a: int):
    bin_a = str(a % 2)
    a = a // 2
    while a != 0:
        bin_a = str(a % 2) + bin_a
        a //= 2
    return bin_a


# =============================================================================
# Sujet 17
# =============================================================================

def exo_S17(tab: list):
    return min(tab)


def separe(tab: list):
    i = 0
    j = len(tab) - 1
    while i < j:
        if tab[i] == 0:
            i += 1
        else:
            tab[i], tab[j] = tab[j], tab[i]
            j -= 1
    return tab


# =============================================================================
# Sujet 18
# =============================================================================

def exo_S18(elt: int, tab: list):
    try:
        return tab.index(elt)
    except ValueError:
        return -1


def insere(a: int, tab: list):
    lst = list(tab)  # l contient les mêmes éléments que tab
    lst.append(a)
    i = -2
    while a < lst[i]:
        lst[i+1] = lst[i]
        lst[i] = a
        i -= 1
    return lst


# =============================================================================
# Sujet 19
# =============================================================================

def exo_S19(n: int, tab: list):
    try:
        return tab.index(n)
    except ValueError:
        return -1


def position_alphabet(lettre: str):
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ALPHABET.find(lettre)


def cesar(message: str, decalage: int):
    resultat = ''
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for lettre in message:
        if lettre in ALPHABET:
            indice = (position_alphabet(lettre)) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat += lettre
    return resultat


# =============================================================================
# Sujet 20
# =============================================================================

def exo_S20(releve: list, date: list):
    return min(releve), date[releve.index(min(releve))]


def inverse_chaine(chaine: str):
    result = ""
    for caractere in chaine:
        result = caractere + result
    return result


def est_palindrome(chaine: str):
    inverse = inverse_chaine(chaine)
    return chaine == inverse


def est_nbre_palindrome(nbre: int):
    chaine = str(nbre)
    return est_palindrome(chaine)

# =============================================================================
# Sujet 21
# =============================================================================


def exo_S21(elt: str or int, tab: int):
    return_val = 0
    while elt in tab:
        return_val += 1
        tab.remove(elt)
    return return_val


def binaine(a: int):
    bin_a = str(a % 2)
    a = a // 2
    while a != 0:
        bin_a = str(a % 2) + bin_a
        a //= 2
    return bin_a


# =============================================================================
# Sujet 22
# =============================================================================

def exo_S22(elt: str or int, tab: list):
    return_val = 0
    while elt in tab:
        return_val += 1
        tab.remove(elt)
    return return_val


def rendu_monnaie_centimes(s_due: int, s_versee: int):
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    rendu = []
    a_rendre = s_versee - s_due
    i = len(pieces) - 1
    while a_rendre > 0:
        if pieces[i] <= a_rendre:
            rendu.append(pieces[i])
            a_rendre -= pieces[i]
        else:
            i -= 1
    return rendu


# =============================================================================
# Sujet 23
# =============================================================================

def exo_S23(phrase: str):
    return_val = {}
    for i in phrase:
        if i not in return_val.keys():
            return_val[i] = 1
        else:
            return_val[i] += 1
    return return_val


def fusion(L1: list, L2: list):
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0]*(n1+n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2:
        if L1[i1] < L2[i2]:
            L12[i] = L1[i1]
            i1 += 1
        else:
            L12[i] = L2[i2]
            i2 += 1
        i += 1
    while i1 < n1:
        L12[i] = L1[i1]
        i1 = i1 + 1
        i += 1
    while i2 < n2:
        L12[i] = L2[i2]
        i2 = i2 + 1
        i += 1
    return L12


# =============================================================================
# Sujet 24
# =============================================================================

def exo_S24(elt: int, tab: list):
    tab.reverse()
    try:
        return_val = len(tab) - tab.index(elt)
    except ValueError:
        return_val = -1
    tab.reverse()
    return return_val()


class AdresseIP:

    def __init__(self, adresse: str):
        self.adresse = adresse

    def liste_octet(self):
        """renvoie une liste de nombres entiers,
           la liste des octets de l'adresse IP"""
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
           réservée, False sinon"""
        return self.adresse == "192.168.0.0" or self.adresse == "192.168.0.255"

    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse
           IP qui suit l’adresse self
           si elle existe et False sinon"""
        if self.liste_octet()[-1] < 254:
            octet_nouveau = self.liste_octet()[-1] + 1
            return AdresseIP('192.168.0.' + str(octet_nouveau))
        else:
            return False

# =============================================================================
# Sujet 25
# =============================================================================


def exo_S25(tab: list):
    return_val = []
    for i in range(len(tab) - 1):
        if tab[i] + 1 == tab[i+1]:
            return_val.append((tab[i], tab[i + 1]))
    return return_val


def propager(M: list, i: int, j: int, val: int):
    if M[i][j] == 0:
        return M

    M[i][j] = val

    # l'élément en haut fait partie de la composante
    if ((i-1) >= 0 and M[i-1][j] == 1):
        propager(M, i - 1, j, val)

    # l'élément en bas fait partie de la composante
    if ((i+1) < len(M) and M[i+1][j] == 1):
        propager(M, i + 1, j, val)

    # l'élément à gauche fait partie de la composante
    if ((j-1) >= 0 and M[i][j-1] == 1):
        propager(M, i, j - 1, val)

    # l'élément à droite fait partie de la composante
    if ((j+1) < len(M) and M[i][j+1] == 1):
        propager(M, i, j + 1, val)


# =============================================================================
# Sujet 26
# =============================================================================

def exo_S26(phrase: str):
    return_val = {}
    for i in phrase:
        if i not in return_val.keys():
            return_val[i] = 1
        else:
            return_val[i] += 1

    maxi = ['', 0]
    for value, key in list(return_val.items()):
        if maxi[1] < key:
            maxi = value, key

    return maxi[0]


def nbLig(image: list):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)


def nbCol(image: list):
    '''renvoie la largeur de l'image'''
    return len(image[0])


def negatif(image: list):
    '''renvoie le négatif de l'image sous la forme
       d'une liste de listes'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(len(image)):
        for j in range(nbCol(image)):
            L[i][j] = 255 - image[i][j]
    return L


# Faute dans l'enoncer (creation de L et resultat exemple)
def binaire(image: list, seuil: int):
    '''renvoie une image binarisée de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inférieure au seuil
       et 1 sinon'''
    L = [[k for k in i] for i in image]
    for i in range(len(image)):
        for j in range(nbCol(image)):
            if L[i][j] < seuil:
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L


# =============================================================================
# Sujet 27
# =============================================================================


def exo_S27(tab: list):
    return_val = 0
    for i in tab:
        return_val += i
    return return_val / len(tab)


coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def affiche(dessin: list):
    ''' affichage d'une grille : les 1 sont représentés par
        des "*" , les 0 par deux espaces "  " '''

    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *", end="")
            else:
                print("  ", end="")
        print()


def zoomListe(liste_depart: list, k: int):
    '''renvoie une liste contenant k fois chaque
       élément de liste_depart'''
    liste_zoom = []
    for elt in liste_depart:
        for i in range(k):
            liste_zoom.append(elt)
    return liste_zoom


def zoomDessin(grille: list, k: int):
    '''renvoie une grille où les lignes sont zoomées k fois
       ET répétées k fois'''
    grille_zoom = []
    for elt in grille:
        liste_zoom = zoomListe(elt, k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom


# =============================================================================
# Sujet 28
# =============================================================================

def exo_S28(a: dict = {}, lettre: str = 'F'):
    a = {'F': ['B', 'G'], 'B': ['A', 'D'], 'A': ['C', 'E'], 'C': ['', ''],
         'D': ['C', 'E'], 'E': ['', ''], 'G': ['', 'I'], 'I': ['', 'H'],
         'H': ['', '']}
    droite, gauche = a[lettre]
    return_val = 1
    if not(gauche and droite):
        return_val = 1

    elif not gauche and droite:
        return_val += exo_S28(a, droite)

    elif gauche and not droite:
        return_val += exo_S28(a, gauche)

    else:
        return_val += exo_S28(a, gauche) + exo_S28(a, droite)

    return return_val


# Faute dans l'enoncer (dans le code : if tab [max] et
# dans le resultat de l'exemple)
def tri_iteratif(tab: list) -> list:
    for k in range(len(tab) - 1, 0, -1):
        imax = 0
        for i in range(0, k):
            if tab[i] > tab[imax]:
                imax = i
        if tab[imax] > tab[k]:
            tab[k], tab[imax] = tab[imax], tab[k]
    return tab


# =============================================================================
# Sujet 29
# =============================================================================

def exo_S29(n: int) -> list:
    return_val = [n]
    result = n
    while result != 1:
        if not result % 2:
            result /= 2
        else:
            result = 3 * result + 1
        return_val.append(result)
    return return_val


def est_parfait(mot: str) -> list:
    dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
            "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15,
            "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
            "W": 23, "X": 24, "Y": 25, "Z": 26}
    # mot est une chaîne de caractères (en lettres majuscules)
    code_c = ""
    code_a = 0
    for c in mot:
        code_c = code_c + str(dico.get(c))
        code_a += dico.get(c)
    code_c = int(code_c)
    if not code_c % code_a:
        mot_est_parfait = True
    else:
        mot_est_parfait = False
    return [code_a, code_c, mot_est_parfait]


# =============================================================================
# Sujet 30
# =============================================================================

def exo_S30(n1: int, n2: int) -> int:
    return_val = 0

    for i in range(abs(n1)):
        return_val += abs(n2)

    if (n1 < 0 and n2 > 0) or (n1 > 0 and n2 < 0):
        return_val = return_val - return_val - return_val

    return return_val


def chercher(T: list, n: int, i: int, j: int) -> list:
    if i < 0 or j >= len(T):
        print("Erreur")
        return None
    if i > j:
        return None
    m = (i + j) // 2
    if T[m] < n:
        return chercher(T, n, i+1, j)
    elif T[m] > n:
        return chercher(T, n, i, j-1)
    else:
        return m
