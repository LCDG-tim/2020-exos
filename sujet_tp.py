# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 21:50:31 2021.

@author: timot
"""


import random as rdm


def conv_bin(n: int) -> tuple:
    """
    Convert a number in binary base.

    >>> conv_bin(9)
    ([1, 0, 0, 1], 4)

    Parameters
    ----------
    n: int
        A int.

    Returns
    -------
    tuple
        The binary number and the number of bits.

    """
    quotient = n
    ret = []
    while quotient > 0:
        ret.append(quotient % 2)
        quotient //= 2
    ret.reverse()
    return ret, len(ret)


def tri_bulles(T: list) -> list:
    n = len(T)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if T[j] > T[j + 1]:
                tmp = T[j]
                T[j] = T[j + 1]
                T[j + 1] = tmp
    return T


def recherche(gene, seq_adn):
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

def tri_selection(tab):
    n = len(tab)
    print(tab, "\n")
    for i in range(n):
        indix_min = tab[i:].index(min(tab[i:])) + i
        if i != indix_min:
            temp = tab[i]
            tab[i] = tab[indix_min]
            tab[indix_min] = temp
    return tab

def plus_ou_moins():
    nb_mystere = rdm.randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99: "))
    compteur = 1
    while nb_mystere != nb_test and compteur < 10:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore: "))
        else:
            nb_test = int(input("Trop grand ! Testez encore: "))
    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print ("Perdu ! Le nombre était ", nb_mystere)

print(tri_selection([rdm.randint(10, 99)
                     for i in range(20)]))


def recherche(elt, tab):
    return_val = []
    while elt in tab:
        return_val.append(tab.index(elt) + len(return_val))
        tab.remove(elt)
    return return_val

print(recherche(3, [3, 2, 1, 3, 2, 1]))

resultats = {'Dupont':{'DS1': [15.5, 4],
    'DM1': [14.5, 1],
    'DS2': [13, 4],
    'PROJET1': [16, 3],
    'DS3': [14, 4]},
    'Durand':{'DS1': [6 , 4],
    'DM1': [14.5, 1],
    'DS2': [8, 4],
    'PROJET1': [9, 3],
    'IE1': [7, 2],
    'DS3': [8, 4],
    'DS4': [15, 4]}}

def moyenne(nom):
    if nom in resultats:
        notes = resultats[nom]
        total_points = 0
        total_coefficients = 0
        for valeurs in notes.values():
            note , coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round(total_points / total_coefficients, 1)
    else:
        return -1

def RechercheMinMax(tab: list) -> dict:
    return {"min": min(tab),
            "max": max(tab)} if len(tab) else {"min": None,
                                               "max": None}


class Carte:
    """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10,
       Valet, Dame, Roi"""
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    """Remplit le paquet de cartes"""
    def remplir(self):
        for i in range(1, 14):
            for j in range(1, 5):
                self.contenu.append(Carte(j, i))

    """Renvoie la Carte qui se trouve à la position donnée"""
    def getCarteAt(self, pos):
        return self.contenu[pos]


unPaquet = PaquetDeCarte()
unPaquet.remplir()
uneCarte = unPaquet.getCarteAt(20)
print(uneCarte.getNom() + " de " + uneCarte.getCouleur())


def moyenne(tab: list) -> float:
    somme = 0
    for i in tab:
        somme += 1
    return somme / len(tab)

def dec_to_bin(a):
    bin_a = str(a % 2)
    a //= 2
    while a != 0:
        bin_a = str(a % 2) + bin_a
        a //= 2
    return bin_a


print(dec_to_bin(83))


def RechercheMin(tab: list) -> int:
    return tab.index(min(tab))


def separe(tab):
    i = 0
    j = len(tab) - 1
    while i < j:
        if tab[i] == 0:
            i += 1
        else:
            tab[i], tab[j] = tab[j], tab[i]
            j -= 1
    return tab


print(separe([1, 0, 1, 0, 1, 0, 1, 0]))


def recherche(elt: int, tab: list) -> int:
    try:
        return tab.index(elt)
    except ValueError:
        return -1


print(recherche(1, [2, 3, 4]))


def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = -2
    while a < l[i]:
      l[i+1] = l[i]
      l[i] = a
      i -= 1
    return l


ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def position_alphabet(lettre):
    return ALPHABET.find(lettre)


def cesar(message, decalage):
    resultat = ''
    for lettre in message:
        if lettre in ALPHABET:
            indice = (position_alphabet(lettre) + decalage) % 26
            resultat += ALPHABET[indice]
        else:
            resultat += lettre
    return resultat


print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !',4))

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def mini(releve, date):
    minir = releve.index(min(releve))
    return releve[minir], date[minir]


print(mini(t_moy, annees))

def inverse_chaine(chaine):
    result = ""
    for caractere in chaine:
       result = caractere + result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return chaine == inverse

def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)


print(inverse_chaine("bac"))

print(est_palindrome("NSI"))

print(est_palindrome("ISN-NSI"))

print(est_nbre_palindrome(214312))

print(est_nbre_palindrome(213312))

def nb_repetitions(elt, tab):
    count = 0
    while elt in tab:
        count += 1
        tab.remove(elt)
    return count

print(nb_repetitions(5,[2,5,3,5,6,9,5]))

print(nb_repetitions('A',[ 'B', 'A', 'B', 'A', 'R']))

print(nb_repetitions(12,[1, '! ',7,21,36,44]))


def recherche(a, t):
    count = 0
    while a in t:
        count += 1
        t.remove(a)
    return count


def rendu_monnaie_centimes(s_due, s_versee):
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


print(rendu_monnaie_centimes(700,700))


print(rendu_monnaie_centimes(112,500))


def occurence_lettres(phrase):
    return_val = {}
    for i in phrase:
        if i not in return_val.keys():
            return_val[i] = 1
        else:
            return_val[i] += 1
    return return_val


print(occurence_lettres("Hello world !"))


def fusion(L1,L2):
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0] * (n1+n2)
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


print(fusion([1, 6, 10], [0, 7, 8, 9]))


def recheche(elt, tab):
    tab.reverse()
    try:
        return_v =  len(tab) - tab.index(elt)
    except ValueError:
        return_v = -1
    tab.reverse()
    return return_v

print(recherche(1,[2,3,4]))

class AdresseIP:

    def __init__(self, adresse):
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


adresse1 = AdresseIP('192.168.0.1')
adresse2 = AdresseIP('192.168.0.2')
adresse3 = AdresseIP('192.168.0.0')

print(adresse1.est_reservee())

print(adresse3.est_reservee())

print(adresse2.adresse_suivante().adresse)


def recherche(tab):
    return_v = []
    for i in range(len(tab) - 1):
        if tab[i] == tab[i + 1] - 1:
            return_v.append(tab[i], tab[i + 1])
    return return_v


def propager(M, i, j, val):
    if M[i][j] == 0:
        return

    M[i][j] = val

    # l'élément en haut fait partie de la composante
    if ((i-1) >= 0 and M[i-1][j] == 1):
        propager(M, i-1, j, val)

    # l'élément en bas fait partie de la composante
    if ((i+1) < len(M) and M[i+1][j] == 1):
        propager(M, i+1, j, val)

    # l'élément à gauche fait partie de la composante
    if ((j-1) >= 0 and M[i][j-1] == 1):
        propager(M, i, j-1, val)

    # l'élément à droite fait partie de la composante
    if ((j+1) < len(M) and M[i][j+1] == 1):
        propager(M, i, j+1, val)


M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]

propager(M, 2, 1, 3)

print(M)


def occurence_max(chaine):
    return_val = {}
    for i in chaine:
        if i not in return_val.keys():
            return_val[i] = 1
        else:
            return_val[i] += 1
    maxi = ("A", 0)
    for car, nb in return_val.items():
        if maxi[1] < nb:
            maxi = car, nb
    return maxi[0]

ch = "je suis en terminale et je passe le bac et je souhaite poursuivre" + \
     " des etudes pour devenir expert en informatique"
print(occurence_max(ch))


def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le négatif de l'image sous la forme
       d'une liste de listes'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] # on créé une image de 0 aux mêmes dimensions que le paramètre image
    for i in range(len(image)):
        for j in range(nbCol(image)):
            L[i][j] = 255 - image[i][j]
    return L

def binaire(image, seuil):
    '''renvoie une image binarisée de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inférieure au seuil
       et 1 sinon'''
    L = [[k for k in i] for i in image] # on crée une image de 0 aux mêmes dimensions que le paramètre image
    for i in range(len(image)):
        for j in range(nbCol(image)):
            if L[i][j] < seuil:
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L

img=[[20, 34, 254, 145, 6], [23, 124, 287, 225, 69],
     [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]

print(nbLig(img))
print(nbCol(img))
print(negatif(img))
print(binaire(img, 120))


def moyenne(lst):
    somme = 0
    for i in lst:
        somme += i
    return somme / len(lst)


coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def affiche(dessin):
    ''' affichage d'une grille: les 1 sont représentés par
        des "*" , les 0 par deux espaces "  " '''
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *",end="")
            else:
                print("  ",end="")
        print()


def zoomListe(liste_depart, k):
    '''renvoie une liste contenant k fois chaque
       élément de liste_depart'''
    liste_zoom = []
    for elt in liste_depart:
        for i in range(k):
            liste_zoom.append(elt)
    return liste_zoom


def zoomDessin(grille, k):
    '''renvoie une grille où les lignes sont zoomées k fois
       ET répétées k fois'''
    grille_zoom = []
    for elt in grille:
        liste_zoom = zoomListe(elt, k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom

affiche(coeur)
affiche(zoomDessin(coeur, 2))


a = {'F': ['B', 'G'], 'B': ['A', 'D'], 'A': ['', ''], 'D': ['C', 'E'],
'C': ['', ''], 'E': ['', ''], 'G': ['', 'I'], 'I': ['', 'H'], 'H': ['', '']}

def taille(arbre, lettre):
    gauche, droite = arbre.get(lettre)
    print(lettre)
    return_val = 1
    if gauche:
        return_val += taille(arbre, gauche)
    if droite:
        return_val += taille(arbre, droite)
    return return_val


print(taille(a, 'F'))


def tri_iteratif(tab):
    for k in range(len(tab) - 1, 0, -1):
        imax = 0
        for i in range(0, k):
            if tab[i] > tab[imax]:
                imax = i
        if tab[imax] > tab[k]:
            tab[k], tab[imax] = tab[imax], tab[k]
    return tab


print(tri_iteratif([41, 55, 21, 18, 12, 6, 25]))


def calcul(n):
    return_val = [n]
    result = n
    while result != 1:
        if not result % 2:
            result //= 2
        else:
            result = 3 * result + 1
        return_val.append(result)

    return return_val


print(calcul(7))


dico = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7,
        "H":8, "I":9, "J":10, "K":11, "L":12, "M":13,
        "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19,
        "T":20, "U":21,"V":22, "W":23, "X":24, "Y":25, "Z":26}

def est_parfait(mot):
    #mot est une chaîne de caractères (en lettres majuscules)
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


print(est_parfait("ALAIN"))


def multiplication(n1, n2):
    return_v = 0
    if n1 < 0:
        for i in range(abs(n1)):
            return_v -= n2
    else:
        for i in range(n1):
            return_v += n2
    return return_v

print(multiplication(3,5))
print(multiplication(-4,-8))
print(multiplication(-2,6))
print(multiplication(-2,0))


def chercher(T,n,i,j):
    if i < 0 or j >= len(T):
        print("Erreur")
        return None
    if i > j:
        return None
    m = (i+j) // 2
    if T[m] < n:
        return chercher(T, n, i+1, j)
    elif T[m] > n:
        return chercher(T, n, i, j-1)
    else:
        return m


print()
print(chercher([1,5,6,6,9,12],7,0,10), "\n")
print(chercher([1,5,6,6,9,12],7,0,5), "\n")
print(chercher([1,5,6,6,9,12],9,0,5), "\n")
print(chercher([1,5,6,6,9,12],6,0,5), "\n")
