from random import *
from numpy import *
from typing import Iterable
Tableau = Iterable

Tab = Tableau[int]


# 1)
def afficher(t: Tab):
    print(t)


# 2)
def remplir_rndm(t: Tab, rndm_min: int, rndm_max: int):
    for n in range(len(t)):
        t[n] = randint(rndm_min, rndm_max)


# 4)
def croissant(t: Tab):
    croiss = True
    for n in range(1, len(t)):
        if t[n] < t[n-1]:
            croiss = False
            break
    return croiss


# 5)
def moyenne(t: Tab):
    som = int(0)
    for n in range(len(t)):
        som += t[n]
    return round(float(som / len(t)), 2)


# 6)
def occurence(t: Tab, o: int):
    occ = int(0)
    for n in range(len(t)):
        if o == t[n]:
            occ += 1
    print("Occurence de {val_o} :".format(val_o=o), occ)


# 8)
def minimum(t: Tab, min_index=0):
    mini = t[min_index]
    for n in range(min_index+1, len(t)):
        if t[n] < mini:
            mini = t[n]
    return mini


# 9) et 10)
def mini_index(t: Tab, min_index=0):
    mini = minimum(t, min_index)
    for n in range(min_index, len(t)):
        if t[n] == mini:
            return n


# 11)
def permutation(t: Tab, ind1: int, ind2: int):
    perm_temp = t[ind1]
    t[ind1] = t[ind2]
    t[ind2] = perm_temp


# 12)
def tri_croissant(t: Tab):
    for n in range(len(t)):  # Pour chaque valeur du tableau
        permutation(t, n, mini_index(t, n))  # On permute la valeur à l'index n
        # Avec la plus petite valeur trouvée à partir de l'index n
        # À n=0, on permute t[0] avec le minimum à partir de l'index 0
        # À n=1, on permute t[1] avec le minimum à partir de l'index 1
        # Et ainsi de suite...
        # Par exemple, à n=15, la fonction mini_index() aura un nombre
        # d'itérations égal à la taille du tableau moins 15


tab1: Tab = zeros(20, int)  # 3)
tab2: Tab = zeros(20, int)  # 3)
remplir_rndm(tab1, 0, 100)  # 3)
remplir_rndm(tab2, 0, 100)  # 3)
afficher(tab1)  # 3)
afficher(tab2)  # 3)
print("Le tableau est trié dans l'ordre croissant :", croissant(tab1))  # 7)
print("Moyenne des valeurs :", moyenne(tab1))  # 7)
occurence(tab1, 42)  # 7)
tri_croissant(tab1)
tri_croissant(tab2)
afficher(tab1)
afficher(tab2)
