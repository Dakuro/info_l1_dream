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
def minimum(t: Tab):
    mini = t[0]
    for n in range(1, len(t)):
        if t[n] < mini:
            mini = t[n]
    return mini


# 9)
def mini_index(t: Tab):
    mini = minimum(t)
    res_index = "Minimum trouvé aux index suivants : "
    for n in range(len(t)):
        if t[n] == mini:
            res_index += str(n) + " "
    return res_index


# 10)
def mini_index_b(t: Tab, i: int):
    mini = minimum(t)
    res_index = "Minimum à partir de {val_i} trouvé aux index suivants : ".format(val_i=i)
    for n in range(i, len(t)):
        if t[n] == mini:
            res_index += str(n) + " "
    return res_index


test_tab1: Tab = zeros(20, int)  # 3)
test_tab2: Tab = zeros(20, int)  # 3)
remplir_rndm(test_tab1, 0, 100)  # 3)
remplir_rndm(test_tab2, 0, 100)  # 3)
afficher(test_tab1)  # 3)
afficher(test_tab2)  # 3)
print("Le tableau est trié dans l'ordre croissant :", croissant(test_tab1))  # 7)
print("Moyenne des valeurs :", moyenne(test_tab1))  # 7)
occurence(test_tab1, randint(0, 100))  # 7)
print("Minimum du tableau :", minimum(test_tab1))  # 8)
print(mini_index(test_tab1))  # 9)
print(mini_index_b(test_tab1, randint(0, 19)))  # 10)
